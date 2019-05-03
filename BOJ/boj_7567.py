'''
그릇
'''


import sys

s = sys.stdin.readline()
score = 10
for i in range(len(s)-2):
    if s[i] == s[i+1]:
        score += 5
    else:
        score += 10
print(score)


## 다른 사람 풀이
lst = list(input())
temp = ''
h = 0
for a in lst:
    if a == temp:
        h += 5
    else:
        h += 10
    temp = a
print(h)