# import sys
# t = int(input())
# for _ in range(t):
#     a,b=map(int,sys.stdin.readline().split())
#     print(a+b)
#
#
# ## 다른 사람 풀이
# import sys
# input()
# for data in sys.stdin:
#     print(data)
#     a, b = data.split()
#     print(int(a) + int(b))


import itertools

c = itertools.combinations(range(1,10),3)
for i in list(c):
    a = map(str,i)
    b = ''.join(a)
    print(b)
