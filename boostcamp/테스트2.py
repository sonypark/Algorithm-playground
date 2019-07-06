from collections import Counter

def eval_pairs(arr):
    c = Counter(arr).most_common()[0]
    val_of_pairs = c[0]
    num_of_pairs = c[1]
    return [val_of_pairs, num_of_pairs]


def solution(arr1,arr2):
    val_of_pair_arr1, num_of_pair_arr1 = eval_pairs(arr1)
    val_of_pair_arr2, num_of_pair_arr2 = eval_pairs(arr2)

    if num_of_pair_arr1 >=5: num_of_pair_arr1 = 4
    if num_of_pair_arr2 >5: num_of_pair_arr2 = 4

    if num_of_pair_arr1 <=1 and num_of_pair_arr2 <=1: return 0
    if num_of_pair_arr1 == num_of_pair_arr2 and val_of_pair_arr1 == val_of_pair_arr2: return 0
    if num_of_pair_arr1 == num_of_pair_arr2 and val_of_pair_arr1 > val_of_pair_arr2: return 1
    elif num_of_pair_arr1 == num_of_pair_arr2 and val_of_pair_arr1 < val_of_pair_arr2: return 2

    if num_of_pair_arr1 > num_of_pair_arr2: return 1
    else: return 2


# arr1 = [1, 5, 7, 2, 9, 13, 10]
# arr2 = [2, 3, 9, 10, 4, 8, 11]
# 0

arr1 = [1, 4, 1, 3, 5, 6, 10]
arr2 = [9, 2, 3, 1, 3, 4, 10]
# 2
# arr1 = [1, 1, 9, 4, 1, 3, 11]
# arr2 = [2, 3, 3, 13, 12, 9, 9]# 1
# arr1 = [1, 4, 9, 4, 1, 10, 13]
# arr2 = [11, 13, 9, 3, 1, 9, 1]
# 2
# arr1 = [1, 4, 4, 4, 1, 10, 4]
# arr2 = [11, 13, 11, 3, 11, 9, 1]
# 1
# arr1 = [1,2,2,3,2,2,2]
# arr2 = [4,5,4,5,4,5,4]
# 2
print(solution(arr1,arr2))