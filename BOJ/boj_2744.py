s = input()
s2 =''
for i in s:
    if i == i.upper():
        i = i.lower()
    else:
        i = i.upper()
    s2 +=i
print(s2)

# 다른 사람 풀이
print(input().swapcase())