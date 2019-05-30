import sys
import collections
s = sys.stdin.readline().rstrip()
count_most_common_alphabet = collections.Counter(s.upper()).most_common()

if len(s) ==1: print(s.upper())

elif count_most_common_alphabet[0][1] != count_most_common_alphabet[1][1]:
    print(count_most_common_alphabet[0][0])
else:
    print('?')


## 다른 사람 풀이 - chr에 대해 공부하자. 아스키코드 공부하기.
s = input().upper()
l = [s.count(chr(c)) for c in range(65, 91)]

m = max(l)
if l.count(m) == 1:
    print(chr(l.index(m)+65))
else:
    print('?')