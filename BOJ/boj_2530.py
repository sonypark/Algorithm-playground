a, b, c = map(int, input().split())
d = int(input())


def AIWatch(a,b,c,d):
    e = (a * 3600) + (b * 60) + c + d
    while e >= 86400:
        e = e - 86400
    hour = e // 3600
    minutes = (e % 3600) // 60
    sec = e % 60

    return print(hour, minutes, sec)
AIWatch(a,b,c,d)
