import sys
ll=[]
for _ in range(8):
    n = int(sys.stdin.readline())
    ll.append(n)
s = sorted(ll)[-5:]
print(sum(s))
for i in range(len(ll)):
    if ll[i] in s:
        print(i+1, end=" ")





