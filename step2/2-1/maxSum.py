# https://www.acmicpc.net/problem/2439

n = int(input())
a = list(map(int, input().split()))

sumList = [a[0]]
for i in range(n-1):
    sumList.append(max(sumList[i]+a[i+1], a[i+1]))
print(max(sumList))


'''
10
10 -4 3 1 5 6 -35 12 21 -1


[10, 6]
[10, 6, 9]
[10, 6, 9, 10]
[10, 6, 9, 10, 15]
[10, 6, 9, 10, 15, 21]
[10, 6, 9, 10, 15, 21, -14]
[10, 6, 9, 10, 15, 21, -14, 12]
[10, 6, 9, 10, 15, 21, -14, 12, 33]
[10, 6, 9, 10, 15, 21, -14, 12, 33, 32] => 연속한 수들의 합의 최댓값이 담긴다.
'''