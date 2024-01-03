""""""
import calendar

"""
Write the number of days in a certain month of a certain year (in modern western calendar).

Input
Line 1: Integer m for the month.
Line 2: Integer y for the year.
Output
Line 1 : The number of days in that month (1-31).
Constraints
1 ≤ m ≤ 12
1600 ≤ y ≤ 2500

Example
Input
3
2010
Output
31

INPUT:
8
1970
OUTPUT:
31

INPUT:
2
2016
OUTPUT:
29

INPUT:
2
1800
OUTPUT:
28

INPUT:
2
2000

OUTPUT:
29

INPUT:
6
1999

OUTPUT:
30

INPUT:
12
1997

OUTPUT:
31
"""

m = int(input())
y = int(input())
days = calendar.monthrange(y, m)
print(days)

# Without build-in function
# m, y = map(int, [input(), input()])
# print(31 if m in[1,3,5,7,8,10,12] else 30 if m in[4,6,9,11] else 29 if m==2 and(y%4==0 and(y%100!=0 or y%400==0)) else 28)

