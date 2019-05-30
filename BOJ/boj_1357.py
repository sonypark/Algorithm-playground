import sys
a,b = sys.stdin.readline().split()
ra = int(''.join(list(reversed(a))))
rb = int(''.join(list(reversed(b))))
print(int(''.join(list(reversed(str(ra+rb))))))


## 다른 사람 풀이
a,b=input().split()
print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))