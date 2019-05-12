n,k = map(int,input().split())
li = [int(i) for i in input().split()]
s = 0
for i in range(0,len(li)):
  if((li%2)!=0):
    s = s+1
    if s == k:
      print(li[i])
  else:
    pass
