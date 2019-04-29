a = int(input())
op = input()
b = int(input())

def noise(a,b):
    if(op == '+'):
        print(a+b)
    else:
        print(a*b)
noise(a,b)
