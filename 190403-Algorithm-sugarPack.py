'''
sugar 가 5로 나누어 떨어지면
    - sugar 에서 5kg을 빼주고 pack_num 를 하나 추가한다.
그렇지 않으면
    - sugar 에서 3kg을 빼주고 pack_num 를 하나 추가한다.
이 과정을 sugar 가 0이 될 때 까지 반복한다
sugar 가 0 밑으로 떨어지면 -1을 출력한다.
'''


sugar = int(input())
pack_num = 0

while(sugar>0):
    if(sugar % 5 == 0):
        sugar -= 5
        pack_num += 1
    else:
        sugar -= 3
        pack_num += 1

    if(sugar < 0):
        print(-1)
        break

if(sugar ==0):
    print(pack_num)

