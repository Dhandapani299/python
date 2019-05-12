import re
b = input()
if re.findall("[a-zA-Z2-9]",b):
  print("No")
else:
  print("Yes")
