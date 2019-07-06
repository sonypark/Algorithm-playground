from collections import Counter

def solution(param):
    c = Counter(param)
    answer = []
    visited = []
    for v in param:
        if v in visited: continue
        val = c.get(v)
        if val >=2:
            answer.append(val)
            visited.append(v)
    if len(answer) ==0: return [-1]
    return answer



# arr = [1, 2, 3, 3, 3, 4, 4]
arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
# arr =[3, 5, 7, 9, 1]

print(solution(arr))