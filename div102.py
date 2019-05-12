import math
def div(a):
  if a % 2 == 0:
    return div(a/2)
  else:
    return math.ceil(a)
a = int(input())
print(div(a))
   
