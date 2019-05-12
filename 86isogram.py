def lcm(m,n):
  if m>n:
    grater = m
  else:
    greater = n
  while(True):
    if((greater % m == 0) and (greater % n == 0)):
      lcm = greater
      break
    greater += 1
  return lcm
num 1 = int(input())
num 2 = int(input())
print(lcm(num,num2))
