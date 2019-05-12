p = input()
m = len(s)
l = []
for i in range(m):
  if int(p[i]) %2 != 0:
    l.append(p[i])
k = len(l)
for i in range(k-1):
  print(l[i],end = '')
print(l[k-1])
