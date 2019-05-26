alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
for i in alphabet:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

## 다른 사람 풀이
a = input()
for i in range(97,123):
    print(a.find(chr(i)))


## 아스키코드 이용
import string
string.ascii_lowercase # 'abcdefghijklmnopqrstuvwxyz'