import sys
n = int(sys.stdin.readline())

for i in range(n):
    a,b = sys.stdin.readline().split()
    idx = int(a)-1
    s = ''.join((b[:idx],b[idx+1:]))
    # print(b[:idx]+b[idx+1:])
