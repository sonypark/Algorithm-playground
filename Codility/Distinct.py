from collections import Counter

def distinct_value(arr):
    a = Counter(arr).keys()
    return len(a)

# arr = [2,1,1,2,3,1]
arr = []
print(distinct_value(arr))