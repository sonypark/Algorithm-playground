import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
l = list(sys.stdin.readline().rstrip())
l.sort()
numA = Counter(l)['A']
numB = Counter(l)['B']

if(numA - numB > 0):
    print('A')
elif(numA - numB < 0):
    print('B')
else:
    print('Tie')


## 다른 사람 풀이 count 함수 이용
people = int(input())
votes = input()
A = votes.count('A')
B = votes.count('B')
if A > B:
    print('A')
elif A == B:
    print('Tie')
else:
    print('B')


## 다른 사람 풀이
n=int(input())
t=input().count('A')
print('B' if n-t>t else ('Tie' if n-t==t else 'A'))

