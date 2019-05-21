import sys
sum = 1
for _ in range(3):
    a = int(sys.stdin.readline())
    sum *= a
for i in range(10):
    print(str(sum).count(str(i)))