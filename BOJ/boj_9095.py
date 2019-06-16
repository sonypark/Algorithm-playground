t = int(input())

def sum_one_two_three(n):
    memo = [None]*(12)
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    for i in range(4,n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n]

for _ in range(t):
    n = int(input())
    print(sum_one_two_three(n))


# 다른 사람 풀이
t = int(input())

for i in range(t):
    n = int(input())
    Memo = [0,1,2,4]
    for i in range(4,n+1):
        Memo.append((Memo[i-1]+Memo[i-2]+Memo[i-3]))

    print(Memo[n])

