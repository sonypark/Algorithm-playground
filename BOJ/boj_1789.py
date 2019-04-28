import sys

n = int(sys.stdin.readline())

for a in range(1, round(n)):
    if(a*(a+1) > 2 * n):
        print(a-1)
        break
