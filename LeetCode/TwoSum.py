
## Approach1.Brute force
## Time complexity O(N)
def twoSum(nums, target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


a = [2, 7, 11, 15]
# a = [3,3]
print(twoSum(a, 6))

## Approach2. Hash Table
## time complexity: O(1)

def twoSum_hash(nums,target):

    hash = {}
    for i, num in enumerate(nums):
        n = target - num
        if n in hash:
            return [hash[n], i]
        else:
            hash[num] = i

print(twoSum_hash(a,9))