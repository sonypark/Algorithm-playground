def maxCounters(N, A):
    answer = [0] * N
    last_update = 0
    max_value = 0

    for i in A:
        if i == N + 1:
            last_update = max_value
        else:
            if answer[i-1] < last_update:
                answer[i-1] = last_update

            answer[i - 1] += 1

            if answer[i-1] > max_value:
                max_value = answer[i-1]

    for j in range(len(answer)):
        if answer[j] < last_update:
            answer[j] = last_update
    return answer


n = 5
a = [3, 4, 4, 6, 1, 4, 4]
print(maxCounters(n, a))

## 시간 복잡도 O(N*M) -- time error
def maxCounters(N,A):
    answer = [0]*N

    for i in A:
        if i == N+1:
            m = max(answer)
            answer = [m] * N
        else:
            answer[i-1] +=1
    return answer
