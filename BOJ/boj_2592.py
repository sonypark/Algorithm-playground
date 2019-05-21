import sys
import collections
ll = []
for _ in range(10):
    n = int(sys.stdin.readline())
    ll.append(n)
print(int(sum(ll)/len(ll)))
print(collections.Counter(ll).most_common()[0][0])
