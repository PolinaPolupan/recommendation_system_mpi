результат работы программы:
```
$ mpirun -np 4 python recommendation_system_mpi.py

Sequential runtime: 700.891 seconds

==================================================
MPI processes: 4
Users: 610
Movies: 9724
==================================================
Sequential runtime : 700.891 sec
Parallel runtime   : 196.871 sec
Speedup            : 3.56
Efficiency         : 0.89

Sample recommendations:

User 1
 Movie 541    Predicted rating 5.00
 Movie 750    Predicted rating 5.00
 Movie 514    Predicted rating 5.00
 Movie 720    Predicted rating 5.00
 Movie 858    Predicted rating 5.00
 Movie 899    Predicted rating 5.00
 Movie 913    Predicted rating 5.00
 Movie 915    Predicted rating 5.00
 Movie 955    Predicted rating 5.00
 Movie 968    Predicted rating 5.00

User 2
 Movie 47     Predicted rating 5.00
 Movie 296    Predicted rating 5.00
 Movie 778    Predicted rating 5.00
 Movie 1206   Predicted rating 5.00
 Movie 1221   Predicted rating 5.00
 Movie 1258   Predicted rating 5.00
 Movie 2712   Predicted rating 5.00
 Movie 4306   Predicted rating 5.00
 Movie 4878   Predicted rating 5.00
 Movie 4896   Predicted rating 5.00

User 3
 Movie 47     Predicted rating 5.00
 Movie 50     Predicted rating 5.00
 Movie 101    Predicted rating 5.00
 Movie 150    Predicted rating 5.00
 Movie 223    Predicted rating 5.00
 Movie 296    Predicted rating 5.00
 Movie 380    Predicted rating 5.00
 Movie 454    Predicted rating 5.00
 Movie 517    Predicted rating 5.00
 Movie 541    Predicted rating 5.00

User 4
 Movie 2289   Predicted rating 5.00
 Movie 28     Predicted rating 5.00
 Movie 53     Predicted rating 5.00
 Movie 85     Predicted rating 5.00
 Movie 99     Predicted rating 5.00
 Movie 104    Predicted rating 5.00
 Movie 163    Predicted rating 5.00
 Movie 175    Predicted rating 5.00
 Movie 281    Predicted rating 5.00
 Movie 283    Predicted rating 5.00

User 5
 Movie 25     Predicted rating 5.00
 Movie 236    Predicted rating 5.00
 Movie 780    Predicted rating 5.00
 Movie 593    Predicted rating 4.65
 Movie 356    Predicted rating 4.41
 Movie 377    Predicted rating 4.20
 Movie 292    Predicted rating 4.05
 Movie 587    Predicted rating 4.00
 Movie 11     Predicted rating 4.00
 Movie 14     Predicted rating 4.00
```
