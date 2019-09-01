def Triangle(A):

    if len(A) <3: return 0

    A.sort()
    for i in range(0, len(A)-2):
        if A[i] +A[i+1] > A[i+2]:
            return 1
    else: return 0

# arr = [10,2,5,1,8,20]
arr = [10,50,5,1]
# arr = []
print(Triangle(arr))