import sys
ll = []
for i in range(7):
    n = int(sys.stdin.readline())
    if(n%2 !=0):
        ll.append(n)

if len(ll) ==0:
    print(-1)
else:
    print(sum(ll))
    print(min(ll))


## filter를 이용한 풀이
ll = list(filter(lambda x: x%2!=0, [int(sys.stdin.readline()) for _ in range(7)]))
if len(ll) ==0:
    print(-1)
else:
    print(sum(ll))
    print(min(ll))
