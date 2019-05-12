def palin(str):
  rev = ''.join(reversed(str))
  if (str == rev):
    return True
  return False
w = input()
ans = palin(w)
if(ans):
  print("yes")
else:
  print("No")
