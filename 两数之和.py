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
# a = Solution()
# a.twoSum(nums, target)

class Solution2:
    def twoSum(self, nums, target):
        nums1 = nums.copy()
        for i in nums1:
            nums1.remove(i)
            # print(nums, nums1)
            if target - i in nums1 and nums.index(i) != nums.index(target - i):
                return ([nums.index(i), nums.index(target - i)])
                
a = Solution2()
print(a.twoSum(nums, target))
end = time.time()
print(star, end)

