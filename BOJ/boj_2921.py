n = int(input())
bottom_up = [None] * (n+1)
bottom_up[1] = 3

for i in range(2, n+1):
    bottom_up[i] = bottom_up[i-1] + int(i*(i+1)*3/2)
print(bottom_up[n])


print(int((n*(n+1)*(n+2))/2))