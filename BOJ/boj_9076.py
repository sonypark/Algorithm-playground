import sys
t = int(input())
for i in range(t):
    score = list(map(int, sys.stdin.readline().split()))
    score.remove(max(score))
    score.remove(min(score))

    if max(score) - min(score) >= 4: print('KIN')
    else: print(sum(score))
