def tapeEquilibrium(A):
    s = sum(A)
    m = 2000
    l_sum = 0
    for i in A[:-1]:
        l_sum += i
        a = abs((l_sum)*2 - s)
        if (m >= a): m = a
    return m

a = [3,1,2,4,3]
print(tapeEquilibrium(a))


# # 시간 초과 O(N*N)
# sum은 O(N)의 시간복잡도를 갖는다.
# for loop 안에 sum을 썼으니 O(N*N)이 되어 시간 초과가 난다.
def tapeEquilibrium(A):
    m = 2000
    for i in range(len(A)-1):
        a = abs(sum(A[:i+1]) - sum(A[i+1:]))
        if (m >= a): m = a
    return m


