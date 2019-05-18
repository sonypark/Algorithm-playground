import sys
n = int(sys.stdin.readline())

for i in range(n):
    t = int(sys.stdin.readline())
    print(sum(map(int, sys.stdin.readline().split())))
