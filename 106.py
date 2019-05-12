n,k = map(int,input().split())
l = [int(i) for i in input().split()]
s = 0
for i in range(0,len(l)):
  if((l%2)!=0):
    s = s+1
    if s == k:
      print(l[i])
  else:
    pass
