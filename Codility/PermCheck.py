from collections import Counter
def permCheck(A):
    n = len(A)
    ss = n*(n+1)/2
    s = sum(A)
    if ss == s:
        c = Counter(A).most_common()
        if c[0][1] >=2: return 0
        return 1
    else: return 0

# arr = [4,1,3]
arr = [1,4,1]
print(permCheck(arr))
