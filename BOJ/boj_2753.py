import sys
c = int(sys.stdin.readline())

def leapYear(c):
    if c % 400 == 0:
        print(1)

    elif c % 4 == 0 and c % 100 !=0:
        print(1)

    else:
        print(0)
leapYear(c)
