
def binaryGap(n):
    b = bin(n)[2:]
    count = 0
    length = []
    for i in b:
        if i =='1':
            length.append(count)
            count = 0
        if i =='0': count +=1
    return max(length)


binaryGap(1041)