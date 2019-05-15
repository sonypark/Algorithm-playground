import sys
ll = [0]
for _ in range(4):
    a,b = map(int, sys.stdin.readline().split())
    ll.append(ll[-1]+b-a)
print(max(ll))


## 다른 사람 풀이
max = 0
p = 0
for _ in range(4):
    a,b = map(int, sys.stdin.readline().split())
    p += b-a

    if max<p:
        max = p
print(max)
