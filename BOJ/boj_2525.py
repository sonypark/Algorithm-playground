a, b = map(int, input().split())
c = int(input())

def ovenWatch(a,b,c):
    d = a * 60 + b + c

    if d >= 1440:
        d = d - 1440

    hour = d // 60
    minutes = d % 60

    return print(hour, minutes)
ovenWatch(a,b,c)