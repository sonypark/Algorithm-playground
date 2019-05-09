'''
전자레인지
버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.
A, B, C 3개의 버튼을 적절히 눌러서 그 시간의 합이 정확히 T초가 되도록 해야 한다.
단 버튼 A, B, C를 누른 횟수의 합은 항상 최소가 되어야 한다. 이것을 최소버튼 조작이라고 한다.

T초를 위한 최소버튼 조작의 A B C 횟수를 첫 줄에 차례대로 출력해야 한다. 각각의 횟수 사이에는 빈 칸을 둔다.
해당 버튼을 누르지 않는 경우에는 숫자 0을 출력해야한다.
만일 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 첫 줄에 출력해야 한다.
'''

s = int(input())

def microwave(s):
    A,B,C= 300,60,10
    a,b,c= 0,0,0

    while(s>0):
        if (s // A !=0):
            a = s // A
            s = s % A
        elif(s // B !=0):
            b = s // B
            s = s % B
        elif(s % C ==0):
            c = s // C
            s = s % C
        else:
            print(-1)
            return
    print(a,b,c)

microwave(s)

## 다른 사람 풀이
## -1인 조건을 먼저 해줘서 불필요한 연산 시간을 줄였다.
n=int(input())
a=0
b=0
c=0
if (n%10): print("-1")
else:
    if (n>=300):
        a=n//300
        n=n%300
    if (n>=60):
        b=n//60
        n=n%60
    if (n>=10):
        c=n//10
        n=n%10
    print(a,b,c)


## 다른 사람 풀이
## 위와 비슷한 풀이지만 좀 더 간단하다.

S=int(input())
L=[0 for i in range(3)]
if S%10:
    print(-1)
else:
    L[0]=S//300;S%=300
    L[1]=S//60;S%=60
    L[2]=S//10
    print(*L)




