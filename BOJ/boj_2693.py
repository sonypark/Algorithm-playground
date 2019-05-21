import sys
t = int(input())

for _ in range(t):
    ll = list(map(int,sys.stdin.readline().split()))
    ll.sort()
    print(ll[-3])
