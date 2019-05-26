alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = input()
answer = []
for i in alphabet:
    count = 0
    for j in sorted(s):
        if i == j:
            count +=1
    answer.append(count)
print(*answer)
