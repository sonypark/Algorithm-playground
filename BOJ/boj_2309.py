import sys
import itertools
ll = [int(sys.stdin.readline()) for _ in range(9)]
ll.sort()
remainder = sum(ll)-100

for c in itertools.combinations(ll,2):
    if sum(c) == remainder:
        ll.remove(c[0])
        ll.remove(c[1])
        break # break 를 꼭 해줘야 된다. 만족하는 값이 여러개 일 수 있기 떄문이다.
for i in ll:
    print(i)