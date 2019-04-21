# https://www.acmicpc.net/problem/1427

a = list(map(str, input()))
a.sort(reverse=True)
print(''.join(a))