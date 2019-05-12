import re
c = input()
if re.findall("[a-zA-Z2-9]",c):
  print("No")
else:
  print("Yes")
