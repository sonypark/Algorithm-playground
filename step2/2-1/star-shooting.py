# https://www.acmicpc.net/problem/1912

a = int(input())

for i in range(1, a+1):
    print((a-i) * ' ' + i * '*')
