import re
str = input()
res = re.findall('[0-9]',str)
for i in res:
  print(i,end='')
