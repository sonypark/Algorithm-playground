import sys
t = int(input())

for _ in range(t):
    s = set()
    people, seat = map(int, sys.stdin.readline().split())
    for _ in range(people):
        seat_number = int(sys.stdin.readline())
        s.add(seat_number)
    print(people - len(s))


