n = int(input())

def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

fact_result = factorial(n)
count = 0
for i in str(fact_result)[::-1]:
    if i == '0':
        count +=1
    else:
        break
print(count)


## 다른 사람 풀이
N=int(input())
a=0
while(N>=5):
    b=int(N/5)
    N/=5
    a+=b
print(a)


#
# ## 배열 이용
# def factorial_bottom_up(n):
#     if n == 0:
#         return 1
#     bottom_up = [None]*(n+1)
#     bottom_up[0] = 1
#     bottom_up[1] = 1
#     bottom_up[2] = 2
#     for i in range(2,n+1):
#         bottom_up[i] = i* bottom_up[i-1]
#     return bottom_up[n]
#
# print(factorial_bottom_up(n))


