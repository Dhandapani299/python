s =input ()
if (len (s) %2 == 0):
  k=len(s)//2
  print(s[:k-1]+'*'+'*'+s[k+1:])
else:
  k = len(s)//2
  print(s[:k]+'*'+s[k+1:])
