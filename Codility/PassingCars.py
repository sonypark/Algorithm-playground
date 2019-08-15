
def passingCars(A):
    s = sum(A)
    pair = 0
    for i in range(len(A)):
        if A[i] ==1:
            s -=1
        if A[i] ==0:
           pair += s
        if pair > 1000000000: return -1
    return pair

a= [0,1,0,1,1]
print(passingCars(a))