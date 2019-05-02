import sys
import collections

n = int(sys.stdin.readline())
answer = []
def counter(n):
    for i in range(n):
        ll = list(map(int, sys.stdin.readline().split()))

        count = collections.Counter(ll)
        mostCommonNum = count.most_common()
        lenOfNum = len(count)
        result = 0
        if lenOfNum == 1:
            result = 10000 + (1000*mostCommonNum[0][0])
        if lenOfNum == 2:
            result = 1000 + (100*mostCommonNum[0][0])
        if lenOfNum == 3:
            result = 100*(max(ll))
        answer.append(result)

counter(n)
print(max(answer))


## 다른 사람 풀이
import sys
n = int(sys.stdin.readline())
value = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    if( l[0] == l[2] ):
        value.append(10000 + l[0]*1000)
    elif( (l[0] == l[1])or(l[1] == l[2]) ):
        value.append(1000 + l[1]*100)
    else:
        value.append( 100 * l[2] )

print(max(value))