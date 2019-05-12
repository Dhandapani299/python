l = []
class rep:
  def printno(self,n,k,l):
    c = 0
    for i in range(n):
      if k == l(i):
        c +=1
    print(c)
n,k = map(int,input().split())
l = list(map(int,input().split()))
a = rep()
a.printno(n,k,l)
