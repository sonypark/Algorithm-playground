import sys
import itertools
ll =[]
for _ in range(9):
    n = int(sys.stdin.readline())
    ll.append(n)
c = itertools.combinations(ll,7)
for i in c:
    if sum(i) == 100:
        for j in i:
            print(j)
            break
