import sys
n = int(sys.stdin.readline())

if n >=90:
    print('A')
elif n >=80 :
    print('B')
elif n >=70:
    print('C')
elif n >=60:
    print('D')
else:
    print('F')


'''
90 ~ 100점은 A, 
80 ~ 89점은 B, 
70 ~ 79점은 C, 
60 ~ 69점은 D, 
나머지 점수는 F를 출력하는 프로그램
'''