import sys
t = int(input())

for _ in range(t):
    s = sys.stdin.readline().rstrip()
    print(s[0], end='')
    print(s[-1])


## 다른 사람 풀이
for _ in range(int(input())):
    s = input()
    print(s[0] + s[-1])