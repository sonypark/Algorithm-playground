import sys
n = int(sys.stdin.readline())

for c in range(n):
    n, *m = map(int, sys.stdin.readline().split())
    m.sort()

    gap = 0
    for i in range(0,len(m)-1):
        s = abs(m[i] - m[i+1])
        if s > gap:
            gap = s
    print('Class %d' % (c+1))
    print('Max %d, Min %d, Largest gap %d' %(max(m), min(m), gap))


