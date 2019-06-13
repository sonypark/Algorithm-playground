def vps(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    r_count = 0
    l_count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == ')': r_count +=1
        if s[i] == '(': l_count +=1
        if l_count > r_count: return False
    if r_count == l_count: return True


n = int(input())

for _ in range(n):
    s = input()

    if (vps(s)):
        print('YES')
    else:
        print('NO')



## 다른 사람 풀이
import sys

def checkVPS(ps):
    st = list()

    for v in ps:
        if v == "(":
            st.append(v)
        else:
            if len(st) == 0:
                return False
            else:
                st.pop()

    if len(st) > 0:
        return False

    return True


TC = int(input())

for _ in range(TC):
    ps = sys.stdin.readline().rstrip()

    if checkVPS(ps) == True:
        print("YES")
    else:
        print("NO")
