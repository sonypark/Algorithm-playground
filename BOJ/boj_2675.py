n = int(input())

for i in range(1,n+1):
    answer = ''
    r, s =input().split()
    r = int(r)
    s = map(lambda e: e, s)
    for j in s:
        answer += ''.join(j * r)
    print(answer)

