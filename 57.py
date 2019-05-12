lst = []
class rep:
  def printno(self,n,k,lst):
    c = 0
    for i in range(n):
      if k == lst(i):
        c +=1
    print(c)
n,k = map(int,input().split())
lst = list(map(int,input().split()))
a = rep()
a.printno(n,k,lst)
