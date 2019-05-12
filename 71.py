def palin(str):
  rev = ''.join(reversed(str))
  if (str == rev):
    return True
  return False
n = input()
ans = palin(n)
if(ans):
  print("yes")
else:
  print("No")
