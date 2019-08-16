
## 시간 초과
## 시간 복잡도 O(N^3)
'''
from itertools import combinations
def maxProductOfThree(A):
    c = combinations(A,3)
    MAX_NUM = A[0]*A[1]*A[2]
    for x,y,z in c:
        m = x * y * z
        if m > MAX_NUM: MAX_NUM = m
    return MAX_NUM
'''

## 시간복잡도 O(N*logN)
def maxProductOfThree(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])


a = [-3,1,2,-2,5,6]
print(maxProductOfThree(a))