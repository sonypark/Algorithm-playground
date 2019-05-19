import sys
_ = input()
# z_list = list(map(int, sys.stdin.readline().split()))
z_list = [int(x) for x in sys.stdin.readline().split()]
n = int(sys.stdin.readline())
print(z_list.count(n))

