
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：只出现一次的数字给定一个非空整数数组，除了某个元素只出现一次以外，
其余每个元素均出现两次。找出那个只出现了一次的元素,不使用额外空间。
作者：ithh
时间：Wed Aug 26 11:08:41 2020
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1 使用count方法，返回列表中元素出现的次数,也可以使用counter(),都会用额外空间
        for i in nums:
            if nums.count(i) == 1:
                return i       
        '''
        执行用时：6884 ms, 在所有 Python3 提交中击败了5.02%的用户
        内存消耗：15.2 MB, 在所有 Python3 提交中击败了92.37%的用户
        '''

        # 2 直接计算得到，不必循环
        return sum(set(nums))*2-sum(nums)

        # 3 做异或运算 快，不用多余空间
        # 异或的性质:两个数字异或的结果a^b是将a和b的二进制每一位进行运算，得出的数字。 
        # 运算的逻辑是如果同一位的数字相同则为 0，不同则为 1
        single_number = 0
        for i in nums:
            single_number ^= i
        return single_number





