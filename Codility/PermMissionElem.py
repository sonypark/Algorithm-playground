def permMissingElem(A):
    n = len(A)
    s = (n+1)*(n+2) / 2
    return int(s - sum(A))


a = [2,3,1,5]
# a = [1,3]
print(permMissingElem(a))

'''
This problem has a mathematical solution, 
based on the fact that the sum of consecutive integers from 1 to n 
is equal to n(n+1)/2.
'''