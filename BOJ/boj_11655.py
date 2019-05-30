s = input()
rot13 = ''
for i in s:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        s_rot13 = ord(i) + 13

        if 78<= ord(i) <=90:
            s_rot13 -= 26

        elif s_rot13>122:
            s_rot13 -= 26
        rot13 +=chr(s_rot13)
    else:
        rot13 +=i
print(rot13)

## 다른 사람 풀이
inputStr = input()

for s in inputStr:
    s = ord(s)
    if 65 <= s <= 90:
        s += 13
        if 90 < s:
            s -= 26
    if 97 <= s <= 122:
        s += 13
        if 122 < s:
            s -= 26

    print(chr(s), end='')