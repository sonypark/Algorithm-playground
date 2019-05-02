'''
알람시계
'''


import sys

a,b = map(int, sys.stdin.readline().split())

c = a * 60 + b - 45
hour = c // 60
minutes = c % 60

if(hour < 0):
    hour = 23
print(hour, minutes)
