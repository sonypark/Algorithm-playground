a = int(input())
b = list(map(int,input()))

three = a * b[2]
four = a * b[1]
five = a * b[0]
six = three + four*10 + five*100

print(three)
print(four)
print(five)
print(six)