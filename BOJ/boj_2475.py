import sys
print(sum([x**2 for x in map(int, sys.stdin.readline().split())]) %10)

## lambda 함수를 이용한 풀이: 콤마(,) 뒤에 리스트를 넣음
print(sum(map(lambda x: int(x)**2, input().split()))%10)
