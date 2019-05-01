'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
'''

import collections
import sys

ll = map(int, sys.stdin.readline().split())

sameNum = collections.Counter(ll)
lenOfsameNum = len(sameNum)
keyList = list(sameNum.keys())
mostCommonNum = sameNum.most_common(1)

if(lenOfsameNum == 1):
    print(10000 + 1000*keyList[0])
if(lenOfsameNum == 2):
    print(1000 + 100*mostCommonNum[0][0])
if(lenOfsameNum == 3):
    print(sorted(keyList)[2]*100)

