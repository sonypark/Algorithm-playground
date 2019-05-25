import sys
t = int(sys.stdin.readline())
for i in range(t):
    _ = input()
    m = list(map(int,sys.stdin.readline().split()))
    print((max(m)-min(m))*2)
