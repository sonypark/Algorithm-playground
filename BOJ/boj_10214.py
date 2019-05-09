'''
연고전
'''

import sys

n = int(sys.stdin.readline())

def baseball(Y, K):
    for _ in range(9):
        y,k = map(int, sys.stdin.readline().split())
        Y.append(y)
        K.append(k)
    return sum(Y) - sum(K)

for _ in range(n):
    Y = []
    K = []

    result = baseball(Y,K)

    if result > 0: print('Yonsei')
    elif result < 0: print('Korea')
    else: print('Draw')
