'''
def frogRiverOne(X,A):
    counting_arr = [0]* (100001)
    counting_arr[0] +=1
    print(counting_arr)
    for i in range(len(A)):
        counting_arr[A[i]] +=1
        if counting_arr[X] !=0:
            for j in counting_arr[:X]:
                if j ==0: break
            return i
    return -1
'''

def frogRiverOne(X,A):
    coverd_time = [-1]*(X+1)
    uncovered_position = X
    for i in range(len(A)):
        if coverd_time[A[i]] != -1: continue
        else:
            coverd_time[A[i]] = i
            uncovered_position -=1
            if uncovered_position ==0: return i
    return -1


# x = 5
# a = [1,3,1,4,2,3,5,4]
x=1
a=[1]
# x=5
# a=[3]
print(frogRiverOne(x,a))