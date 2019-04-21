# https://www.acmicpc.net/problem/1463

n = int(input())


# 이렇게 하면 런타임 에러난다. (시간초과)
# arr_min[0] = 0 이런식으로 넣는 것보다 append로 넣는게 더 빠르다.
def dto1(n):
    arr_min = [None] * (n+1) # n일 때 나누어 떨어지는 최소 횟수를 기록하는 공간
    arr_min[0] = 0
    arr_min[1] = 0  # 1 일때 횟수 0
    arr_min[2] = 1  # 2일때 1로 한번에 나누어 떨어지므로 횟수 1
    arr_min[3] = 1  # 2일때 1로 한번에 나누어 떨어지므로 횟수 1

    for i in range(4, n+1):
        arr_min[i] = arr_min[i-1] + 1 # 1을 뺸다. 1은 이전 최솟값이 된다. 즉, 1을 빼고(횟수 1증가) 이전 최솟값에 더하면 된다.
        if(i % 2 == 0):  # 2로 나누어 떨어지는 경우
            arr_min[i] = min(arr_min[i], (arr_min[i // 2] + 1))  # 이미 있는 값과, 2로 나눈값을 비교하여 최소값을 넣는다.
                                                                # 2로 나눌 경우 계산을 하는 것이므로 횟수 +1 카운트 해줘야한다.
        if(i % 3 == 0):
            arr_min[i] = min(arr_min[i], (arr_min[i // 3] + 1))
    # print(arr_min)
    return arr_min[n]

print(dto1(n))


# append로 배열에 넣는게 더 빠르다. (640ms)
n = int(input())

dp = []

dp.append(0)  # 0
dp.append(0)  # 1
dp.append(1)  # 2
dp.append(1)  # 3

for i in range(4, n + 1):
    dp.append(dp[i - 1] + 1); # 1을 빼고 최소 연산의 개수 계산

    if(i % 2 == 0): # 2로 나눠진다면
        dp[i] = min(dp[i], dp[i // 2] + 1) # 비교
    if(i % 3 == 0): # 3으로 나눠진다면
        dp[i] = min(dp[i], dp[i // 3] + 1) # 비교

print(dp[n])



# 같은 로직이라도 함수로 만드는게 더 빠르다.(500ms)
n = int(input())

def dto1(n):
    arr_min = []
    arr_min.append(0)
    arr_min.append(0)
    arr_min.append(1)
    arr_min.append(1)

    for i in range(4, n + 1):
        arr_min.append(arr_min[i - 1] + 1)
        if (i % 2 == 0):
            arr_min[i] = min(arr_min[i], (arr_min[i // 2] + 1))

        if (i % 3 == 0):
            arr_min[i] = min(arr_min[i], (arr_min[i // 3] + 1))
    return arr_min[n]
print(dto1(n))