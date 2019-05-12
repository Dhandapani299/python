s = input ()
l = []
for i in range(0,len(s)):
  l.append(ord(s[i]))
l.sort()
for i in l:
  print(chr(i),end = '')
