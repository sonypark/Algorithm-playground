
def self_num(n):
    s = n
    for i in str(n):
        s +=int(i)
    return s

num_list = [i for i in range(1,10001)]

for k in range(1,10001):
    if self_num(k) in num_list:
        num_list.remove(self_num(k))
for w in num_list:
    print(w)


## 다른 사람 풀이
def makeSelf(a):
    b = a
    while a > 0:
        b += a%10
        a = a//10
    return b

ls = [1]*10001

for n in range(1,10001):
    k = makeSelf(n)
    if k >10000:
        continue
    ls[k] = 0

for n in range(1,10001):
    if ls[n] == 1:
        print(n)