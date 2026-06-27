from mpi4py import MPI
import pandas as pd
import numpy as np
import time
from sklearn.metrics.pairwise import cosine_similarity


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    ratings = pd.read_csv("ratings.csv")

    rating_matrix = ratings.pivot_table(
        index="userId",
        columns="movieId",
        values="rating",
        fill_value=0
    )

    users = rating_matrix.index.tolist()
    movies = rating_matrix.columns.tolist()

else:
    rating_matrix = None
    users = None
    movies = None

rating_matrix = comm.bcast(rating_matrix, root=0)
users = comm.bcast(users, root=0)
movies = comm.bcast(movies, root=0)

similarity = cosine_similarity(rating_matrix.values)

similarity_df = pd.DataFrame(
    similarity,
    index=users,
    columns=users
)

def recommend(user_id, k_neighbors=5, top_n=10):

    sims = similarity_df.loc[user_id].drop(user_id)

    nearest = sims.nlargest(k_neighbors)

    predictions = {}

    for movie in movies:

        if rating_matrix.loc[user_id, movie] != 0:
            continue

        numerator = 0.0
        denominator = 0.0

        for neighbor, sim in nearest.items():

            rating = rating_matrix.loc[neighbor, movie]

            if rating > 0:
                numerator += sim * rating
                denominator += abs(sim)

        if denominator > 0:
            predictions[movie] = numerator / denominator

    recommendations = sorted(
        predictions.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:top_n]

if rank == 0:

    start = time.time()

    sequential_results = {}

    for user in users:
        sequential_results[user] = recommend(user)

    sequential_time = time.time() - start

    print()
    print("Sequential runtime:", round(sequential_time,3),"seconds")

if rank == 0:
    chunks = np.array_split(users, size)
else:
    chunks = None

local_users = comm.scatter(chunks, root=0)

comm.Barrier()

start = MPI.Wtime()

local_results = {}

for user in local_users:
    local_results[user] = recommend(user)

comm.Barrier()

parallel_time = MPI.Wtime() - start

all_results = comm.gather(local_results, root=0)
times = comm.gather(parallel_time, root=0)

if rank == 0:

    parallel_results = {}

    for r in all_results:
        parallel_results.update(r)

    parallel_runtime = max(times)

    speedup = sequential_time / parallel_runtime
    efficiency = speedup / size

    print()
    print("="*50)
    print("MPI processes:", size)
    print("Users:", len(users))
    print("Movies:", len(movies))
    print("="*50)

    print(f"Sequential runtime : {sequential_time:.3f} sec")
    print(f"Parallel runtime   : {parallel_runtime:.3f} sec")
    print(f"Speedup            : {speedup:.2f}")
    print(f"Efficiency         : {efficiency:.2f}")

    print("\nSample recommendations:\n")

    sample_users = users[:5]

    for user in sample_users:

        print(f"User {user}")

        for movie, score in parallel_results[user]:
            print(f" Movie {movie:<6} Predicted rating {score:.2f}")

        print()