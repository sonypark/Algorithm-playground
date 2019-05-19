import sys
input()
m = sorted(list(map(int, sys.stdin.readline().split())))
if len(m) ==1: print(m[0]*m[0])
else: print(m[0]*m[-1])

## 다른 사람 풀이
input()
A=[*map(int,input().split())]
print(min(A)*max(A))