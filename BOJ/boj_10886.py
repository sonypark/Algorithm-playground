'''
0 = not cute / 1 = cute
'''
import sys
n = int(sys.stdin.readline())
ll = []
for _ in range(n):
    s = int(sys.stdin.readline())
    ll.append(s)
one = ll.count(1)
zero = ll.count(0)

if one > zero: print('Junhee is cute!')
if one < zero: print('Junhee is not cute!')


## 다른 사람 풀이
import sys
n = int(sys.stdin.readline())
cute = 0
not_cute = 0
for i in range(n):
    vote = int(sys.stdin.readline())
    if vote == 1:
        cute += 1
    else:
        not_cute += 1
if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")