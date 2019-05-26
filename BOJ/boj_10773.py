import sys
n =int(input())
ll = []
for _ in range(n):
    s = int(sys.stdin.readline())
    if s == 0:
        ll.pop()
    else:
        ll.append(s)
print(sum(ll))
