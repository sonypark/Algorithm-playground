# def missingInteger(A):
#     A.sort()
#     m = A[0]
#     if len(A) ==1:
#         if m >= 0 and m > 1: return 1
#         elif m<0: return 1
#
#     if m>=0 and m > 1: return 1
#
#     for i in A:
#         if i >=0:
#             if m+1 ==i:
#                 m = i
#     if m+1 <=0: return 1
#     return m+1

def missingInteger(A):
    n = len(A)
    m = [False]*(n+1)

    for i in range(n):
        if 1<=A[i]<=n:
            m[A[i]-1] = True
    for j in range(len(m)):
        if m[j] == False:
            return j+1

## 다른 사람 풀이

def solution(A):
    ''' Solve it with Pigeonhole principle.
        There are N integers in the input. So for the
        first N+1 positive integers, at least one of
        them must be missing.
    '''
    # We only care about the first N+1 positive integers.
    # occurrence[i] is for the integer i+1.
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item-1] = True
    # Find out the missing minimal positive integer.
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1
    raise Exception("Should never be here.")
    return -1

# a= [1,3,6,4,1,2]
# a= [1,2,3]
# a=[-1,-3]
# a= [3,4,5]
# a=[-5,1,2,5]
# a=[0]
# print(solution(a))

