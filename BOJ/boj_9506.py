'''
약수들의 합

어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
'''


import sys

def perfectNum(ll,s,n):
    if (s == n):
        answer = "%d = " % (s)
        ll.sort()
        for j in ll:
            answer += "%d + " % (j)
        print(answer[:-2])
    else:
        print("%d is NOT perfect." % (n))

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break

    ll = []
    # for i in range(1,round(n/2)+1): # n/2 가 아니라 n의 제곱근까지만 계산하는 게 더 빠르다.
    for i in range(1,int(n ** 0.5)+1):
        if(n % i ==0):
            a = n // i
            if(i == a):
                ll.append(i)
            elif (a not in ll) :
                ll.append(i)
                ll.append(a)
    ll.remove(n)
    s = sum(ll)
    perfectNum(ll,s,n)


## 다른 사람 풀이
def get_measure(input_num):
    ret = []
    for i in range(1, int(input_num ** 0.5) + 1):
        if input_num % i == 0:
            ret.append(i)
            ret.append(input_num // i)
    ret.sort()
    ret.pop()
    return ret


def verify(input_num, measure_list):
    if sum(measure_list) == input_num:
        return True
    return False


n = int(input())
while n != -1:
    measureList = get_measure(n)
    if verify(n, measureList):
        print(str(n) + " = " + " + ".join(map(str, measureList)))
    else:
        print(str(n) + " is NOT perfect.")
    n = int(input())
