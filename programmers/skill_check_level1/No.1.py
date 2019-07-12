

def solution(arr,divisor):
    answer =[]
    for i in arr:
        if i % divisor ==0:
            answer.append(i)
    if len(answer) == 0: return [-1]
    return sorted(answer)

arr = [5,9,7,10]
d = 5
# arr = [2,36,1,3]
# d = 1
# arr = [3,2,6]
# d = 10
print(solution(arr,d))