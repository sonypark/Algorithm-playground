import sys
n = int(input())
a = [int(x) for x in sys.stdin.readline().split()]
print((sum(a)*100 / max(a))/n)



