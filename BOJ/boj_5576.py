import sys

w = [int(sys.stdin.readline()) for _ in range(10)]
k = [int(sys.stdin.readline()) for _ in range(10)]
w.sort()
k.sort()
print(sum(w[-3:]), sum(k[-3:]))