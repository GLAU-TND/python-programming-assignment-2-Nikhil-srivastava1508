def maxl(l,n):
      c=0
      r=0
      for i in range(0,n):
            if(l[i]==0):
                  c=0
            else:
                  c=c+1
                  r=max(r,c)
      return r
j=int(input())
k=str(bin(j))[2:]
l=[int(i) for i in str(k)]
n=len(l)
print(maxl(l,n))
