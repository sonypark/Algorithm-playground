import sys
n = int(sys.stdin.readline())


## 메모리 초과 (실패)
def sortNum3(n):
    ll =[]
    for i in range(1, n+1):
        ll.append(int(sys.stdin.readline()))

    for j in sorted(ll):
        print(j)
# sortNum3(n)


## Memorization 사용 (성공)
def sortNum3_memo(n):
    ll = [0]*10001 # 주어지는 수의 크기 범위만큼 리스트 길이를 만든다.
    for _ in range(n):
        i = int(sys.stdin.readline())
        ll[i] = ll[i] + 1

    for j in range(len(ll)):
        if (ll[j] != 0):
            for m in range(ll[j]):
                print(j)

sortNum3_memo(n)

## Dictionary 사용 (성공)
def sortNum3_dic(n):
    dic = {}
    for _ in range(n):
        i = int(sys.stdin.readline())
        if i in dic:
            dic[i] = dic[i] + 1
        else:
            dic[i] = 1

    for j in sorted(dic.items()):
        for _ in range(j[1]):
            print(j[0])
# sortNum3_dic(n)

