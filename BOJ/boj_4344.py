import sys
t = int(input())

for _ in range(t):
    a = list(map(int, sys.stdin.readline().split()))
    n = a[0]
    b = a[1:]
    avr = sum(b) / n
    count = 0
    for i in b:
        if i > avr:
            count += 1
    answer = count / n * 100
    print('{:.3f}%'.format(answer))


## 다른 사람 풀이

n = int(input())

def higher_mean(x):
    average = sum(x[1:])/x[0]
    count = len([c for c in x[1:] if c > average])
    percentage =  count/x[0]*100
    print(str('%.3f' % round(percentage,3)) +"%")

for i in range(n):
    x = list(map(int,input().split(" ")))
    higher_mean(x)

