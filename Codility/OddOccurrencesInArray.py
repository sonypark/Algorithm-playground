from collections import Counter

# def OddOccurrencesInArray(A):
#     a = Counter(A).most_common()
#     return a[-1][0]

def OddOccurrencesInArray(A):
    result = 0
    for e in A:
        print(result, e)
        print(result ^ e)
        result = result ^ e
    return result
arr = [9,3,9,3,9,7,9]
# arr = [1,1,2,2,9,3,9,3,9,7,9]
# arr = [1, 2, 1, 3, 5, 2, 3, 1, 1, 2, 2 ]
# arr = [1000000, 2000000, 1000000, 30000000, 5000000, 2000000, 30000000]
print(OddOccurrencesInArray(arr))
