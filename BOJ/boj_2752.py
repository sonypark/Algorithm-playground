import sys
for x in sorted(map(int, sys.stdin.readline().split())):
     print(x, end=" ")

## 다른 사람 풀이
print(*sorted(map(int,input().split())))