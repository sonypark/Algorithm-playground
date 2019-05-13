import sys
n,x = list(map(int, input().split()))
m = map(int, sys.stdin.readline().split())
for i in m:
    if i < x:
        print(i, end=" ")


