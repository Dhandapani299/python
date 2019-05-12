import math
def square(x):
  sr = math.sqrt(x)
  return((sr - math.floor(sr)) == 0 )
x = int()
if (square(x)):
  print("Yes")
else:
  print("No")
