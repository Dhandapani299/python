import math
a = int(input())
for i in range(a):
  if 2 ** i == a:
    f = i
    break
print(2**(f+1))
