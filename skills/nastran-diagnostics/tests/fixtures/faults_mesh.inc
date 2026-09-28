$ ---- plate B: large-field grids, free-field elements, SI steel (mixed units)
$ not connected to plate A; its edge x=2 coincides with plate A's edge
GRID*                101                             2.0             0.0
*                     0.
GRID*                102                             3.0             0.0
*                     0.
GRID*                103                             4.0             0.0
*                     0.
GRID*                104                             2.0             1.0
*                     0.
GRID*                105                             3.0             1.0
*                     0.
GRID*                106                             4.0             1.0
*                     0.
GRID*                107                             2.0             2.0
*                     0.
GRID*                108                             3.0             2.0
*                     0.
GRID*                109                             4.0             2.0
*                     0.
CQUAD4,11,2,101,102,105,104
CQUAD4,12,2,102,103,106,105
CQUAD4,13,2,104,105,108,107
CQUAD4,14,2,105,106,109,108
PSHELL  2       2       1.      2
MAT1    2       2.1+11          .3      7850.
