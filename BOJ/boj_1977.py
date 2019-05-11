import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

ll = []
for n in range(a,b+1):
    sqrt_n = str(n ** 0.5).split('.')
    if (sqrt_n[1] == '0'):
       ll.append(n)

if (len(ll) != 0):
    print(sum(ll))
    print(min(ll))
else:
    print(-1)



