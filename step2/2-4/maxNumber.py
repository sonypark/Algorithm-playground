# https://programmers.co.kr/learn/courses/30/lessons/42746

def maxNumber(numbers):
    numbers.sort()
    print(numbers)

    s = list(map(str, numbers))
    print(s)

    answer = []
    for i in s:
        print(i[0])

n = [6, 10, 2]	# 6210
n2 = [3, 30, 34, 5, 9]	# 9534330
maxNumber(n2)