# https://www.acmicpc.net/problem/2953

a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())
d = map(int, input().split())
e = map(int, input().split())

list = [sum(a), sum(b), sum(c), sum(d), sum(e)]
max_v = max(list)
print(list.index(max_v)+1, max_v)
