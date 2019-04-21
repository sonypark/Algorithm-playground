# https://programmers.co.kr/learn/courses/30/lessons/42748

def kthNumber(array, commands):

    answer = []

    for c in commands:

        s = c[0] - 1
        e = c[1]
        k = c[2] - 1
        answer.append(sorted(array[s:e])[k])

    return answer

a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(kthNumber(a,c))

