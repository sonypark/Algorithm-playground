import sys
t = int(input())

for _ in range(t):
   a,b = map(int, sys.stdin.readline().split())
   zero_count = 0

   for i in range(a,b+1):
       zero_count += int(str(i).count('0'))
   print(zero_count)

## 다른 사람 풀이
K=[str(i).count('0') for i in range(1000001)]
for _ in range(int(input())):
	N,M=map(int,input().split())
	print(sum(K[N:M+1]))