import sys

n = 5
def average(n):
    ll = []
    for i in range(n):
        a = int(sys.stdin.readline())
        if a < 40:
            a = 40
        ll.append(a)
    print(int(sum(ll) / len(ll)))
average(n)