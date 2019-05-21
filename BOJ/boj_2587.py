import sys
ll = []
for _ in range(5):
    n = int(sys.stdin.readline())
    ll.append(n)
print(sum(ll)//len(ll))
print(sorted(ll)[2])

