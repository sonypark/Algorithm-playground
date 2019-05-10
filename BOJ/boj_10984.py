'''
G는 {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3} 중 하나
'''

import sys
n = int(sys.stdin.readline())

for _ in range(n):
    credit = []
    score = []
    m = int(sys.stdin.readline())
    for _ in range(m):
        a,b = sys.stdin.readline().split()
        credit.append(int(a))
        score.append(float(b) * int(a))
    sum_credit = sum(credit)
    print(sum_credit, round(sum(score)/sum_credit,1))
