import sys
n = int(input())

for _ in range(n):
    x,y = sys.stdin.readline().rstrip().split()
    print('Distances: ', end='')
    for i in range(len(x)):
        if (ord(x[i]) > ord(y[i])):
            print(ord(y[i]) + 26 - ord(x[i]), end=' ')
        else:
            print(ord(y[i]) - ord(x[i]), end=' ')
    print()

