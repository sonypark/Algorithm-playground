import sys
a,b,c = map(int, sys.stdin.readline().split())

ll = [a,b,c]
print(sorted(ll)[1])

'''
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 
'''