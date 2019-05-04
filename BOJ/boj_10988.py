# import sys
# s = sys.stdin.readline().rstrip()
# tmp = ''
# for i in s:
#     tmp = i + tmp
# if tmp == s:
#     print(1)
# else:
#     print(0)
#
#
# ## 다른 사람 풀이
# a=input()
# b=a[::-1]
# if a==b:
#     print(1)
# else :
#     print(0)
#
# print(''.join(reversed(s)))


a = '123456789'
print(a[:-3:-1])