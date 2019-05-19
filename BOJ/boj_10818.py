import sys
_ = input()
z_list = [int(x) for x in sys.stdin.readline().split()]
print(min(z_list),max(z_list))
