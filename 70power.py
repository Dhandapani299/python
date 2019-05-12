import math
b = int(input())
for i in range(b):
  if 2 ** i == b:
    f = i
    break
print(2**(f+1))
