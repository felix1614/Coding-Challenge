""""""
"""
You have to activate the parachute of your space vehicle, all the instruments are broken except a three axis accelerometer.
You must open your parachute only once in the atmosphere. If you open it too early your parachute will burn up during re-entry. If you open it too late you will have too much speed and it will be torn appart.
You open the command terminal and decide to code an algorithm that triggers the opening as soon as the acceleration is higher or equal to 9 m/s^2.
The acceleration of the spacecraft is equal to the square root of the sum of squares axes values.

INPUT
line 1 : N the number of measurement point
line N: X Y Z three floating numbers representing the accelerometer measurements in m/s^2

Output:
Line N : for each line given as input return 'WAIT' or 'OPEN'.

Constraints
1 ≤ N ≤ 100
0 <= x,y,z <= 100

Example: 
Input
10
0.0000 0.0000 0.0000
0.0000 0.0000 1.0900
0.0000 0.0000 2.1800
0.0000 0.0000 3.2700
0.0000 0.0000 4.3600
0.0000 0.0000 5.4500
0.0000 0.0000 6.5400
0.0000 0.0000 7.6300
0.0000 0.0000 8.7200
0.0000 0.0000 9.8100

Output
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
OPEN

TEST-2
INPUT:
10
0.0000 0.0000 0.0000
0.5450 0.9440 0.0000
1.0900 1.8879 0.0000
1.6350 2.8319 0.0000
2.1800 3.7759 0.0000
2.7250 4.7198 0.0000
3.2700 5.6638 0.0000
3.8150 6.6078 0.0000
4.3600 7.5517 0.0000
4.9050 8.4957 0.0000

OUTPUT:
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
OPEN

TEST-3
INPUT:
12
-0.0000 0.0000 0.0000
-0.6068 1.0511 0.7007
-1.2137 2.1021 1.4014
-1.8205 3.1532 2.1021
-2.4273 4.2043 2.8029
-3.0342 5.2554 3.5036
-3.6410 6.3064 4.2043
-4.2479 7.3575 4.9050
-4.2479 7.3575 4.9050
-4.2479 7.3575 4.9050
-4.2479 7.3575 4.9050
-4.2479 7.3575 4.9050

OUTPUT:
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
OPEN
OPEN
OPEN
OPEN
OPEN

TEST-4
INPUT:
20
0.0000 0.0000 0.5000
0.4090 0.1329 1.3237
1.0859 0.7890 1.8475
1.5100 2.0784 1.8665
1.1953 3.6789 1.2569
0.0000 4.9591 0.0000
-1.7195 5.2922 -1.8080
-3.2064 4.4132 -3.9633
-3.6304 2.6377 -6.1765
-2.5058 0.8142 -8.1091
-0.0000 0.0000 -9.4182
2.8831 0.9368 -9.3299
4.6649 3.3893 -7.9365
4.6649 6.4207 -5.7662
2.8831 8.8732 -3.0315
0.0000 9.8100 -0.0000
-2.8831 8.8732 3.0315
-4.6649 6.4207 5.7662
-4.6649 3.3893 7.9365
-2.8831 0.9368 9.3299

OUTPUT:
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
WAIT
OPEN
OPEN
OPEN
OPEN
OPEN
OPEN
OPEN
OPEN
OPEN
OPEN
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x, y, z = [float(j) for j in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("Answer")
