
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：第9题 回文数 采用数学解法，不转化成字符串
作者：ithh
时间：Thu Aug 27 14:54:46 2020
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        num = 0
        while x > num :
            num = num * 10 + x % 10
            x //= 10
        print(x,num)
        return x == num or x == num // 10

s = Solution()
print(s.isPalindrome(11))

# 注意python运算中地板除