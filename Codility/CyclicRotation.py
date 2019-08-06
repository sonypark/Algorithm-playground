def CyclicRotation(A,K):
    length = len(A)
    answer = [0] * length
    if K == length or length ==0: return A
    d = K % length
    for i in range(length):
        answer[(i+d) % length] = A[i]
    return answer

arr = [3, 8, 9, 7, 6]
arr = []
print(CyclicRotation(arr,2))