import sys

n = int(sys.stdin.readline())


def gcm(a,b):
    a,b = max(a,b), min(a,b)

    remainder = a % b

    while remainder > 0:
        a = b
        b = remainder
        remainder = a % b

    return b  # 최대공약수


for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    lcm = int(a*b / gcm(a,b))
    print(lcm)

