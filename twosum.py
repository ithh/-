import time

class Solution1:
    def twoSum(self, nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]

star = time.time()
nums = [2, 2]
target = 4
a = Solution()
a.twoSum(nums, target)
end = time.time()
print(end-star )

