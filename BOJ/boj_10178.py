import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    print('You get %d piece(s) and your dad gets %d piece(s).' % (a // b, a % b))
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(a // b, a % b))