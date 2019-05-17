import sys
for _ in range(3):
    m = sys.stdin.readline().split()
    count_zero = m.count('0')
    if count_zero == 1: print('A')
    if count_zero == 2: print('B')
    if count_zero == 3: print('C')
    if count_zero == 4: print('D')
    if count_zero == 0: print('E')


## 다른 사람 풀이
b = ['D', 'C', 'B', 'A', 'E']
for i in range(3):
    print(b[sum(list(map(int ,input().split())))])