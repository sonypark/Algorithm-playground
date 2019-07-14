import sys
from itertools import combinations

while True:
    n, *s = list(map(int, sys.stdin.readline().split()))
    if len(s) == 0: break

    d = list(combinations(s,6))
    for i in d:
        print(*i)
    print()
