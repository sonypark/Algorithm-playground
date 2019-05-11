import sys

a,b,c = map(int, sys.stdin.readline().split(':'))
d,e,f = map(int, sys.stdin.readline().split(':'))

a = a * 60 * 60
b = b * 60
c = c

d = d * 60 * 60
e = e * 60
f = f

now = a+b+c
mission = d+e+f

# 만약 현재시간이 미션시간보다 크다면
# 미션시간에 +24시간을 해준다
if now > mission:
    mission += 24*60*60
s = mission - now

h = s // 3600
m = (s % 3600) // 60
sec = s % 60

print('{:0>2d}'.format(h) + ':' '{:0>2d}'.format(m) + ':' '{:0>2d}'.format(sec))