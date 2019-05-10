import sys
n = int(sys.stdin.readline())

for i in range(n):
    t = int(sys.stdin.readline())
    price = []
    player = []
    for _ in range(t):
        a,b = sys.stdin.readline().split()
        price.append(int(a))
        player.append(b)
    idx = price.index(max(price))
    print(player[idx])
