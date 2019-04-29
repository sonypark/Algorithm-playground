'''
화성 수학
@는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.
'''
n = int(input())

answer = 0
for i in range(1, n+1):
    p = input().split()
    a = float(p.pop(0))
    answer += a
    for j in p:
        if j == '@':
            answer *= 3
        if j == '%':
            answer += 5
        if j == '#':
            answer -= 7
    print('%0.2f' % answer)  # or print('{:.2f}'.format(answer))
    answer = 0




'''
Number  	Format	Output	Description
3.1415926	{:.2f}	3.14	2 decimal places
3.1415926	{:+.2f}	+3.14	2 decimal places with sign
-1      	{:+.2f}	-1.00	2 decimal places with sign
2.71828	    {:.0f}	3	    No decimal places
5	        {:0>2d}	05	    Pad number with zeros (left padding, width 2)
5       	{:x<4d}	5xxx	Pad number with x’s (right padding, width 4)
10	        {:x<4d}	10xx	Pad number with x’s (right padding, width 4)
'''