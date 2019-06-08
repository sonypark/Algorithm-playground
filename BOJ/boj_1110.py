s = input()

if int(s) < 10:
    s+='0'

copy_s = s
count = 1
s2 = int(copy_s[0]) + int(copy_s[-1])
copy_s = copy_s[-1] + str(s2)[-1]
while s != copy_s:
    s2 = int(str(copy_s)[0]) + int(str(copy_s)[-1])
    copy_s = str(copy_s)[-1] + str(s2)[-1]
    count +=1
print(count)



## 다른 사람 풀이
n=int(input())
a=-1
cnt=0
while a!=n:
    if cnt==0: a=n
    a=(a%10)*10+(a//10+a%10)%10
    cnt+=1
print(cnt)