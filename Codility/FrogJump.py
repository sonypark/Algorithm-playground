def frogJump(X, Y, D):
    m = Y -X
    if m % D ==0: return m // D
    else: return (m // D) +1

x= 10
y= 85
d= 30


print(frogJump(x,y,d))