import sys
n,b = map(int, sys.stdin.readline().split())

ll =[]
m = int(n**0.5)+1
for i in range(1,m):
    if(n % i ==0):
      j = n // i
      if i !=j:
        ll.append(i)
        ll.append(j)
      else:
          ll.append(i)
ll.sort()

if(len(ll) > b-1):
    print(ll[b-1])
else: print(0)

## 다른 사람 풀이
n,k=input().split()
n=int(n)
k=int(k)
l=[]
for x in range(1,n+1):
    if(n%x==0):
        l.append(x)
if(len(l)<k):
    print(0)
else:
    print(l[k-1])


## 다른 사람 풀이2
N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        exit()
print(0)