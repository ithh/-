
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射与电话按键相同
作者：ithh
时间：Wed Aug 26 13:40:14 2020
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 1
        if not digits: return []
        dic = {
            '2':'abc', '3':'def','4':'ghi', 
            '5':'jkl', '6':'mno', '7':'pqrs', 
            '8':'tuv', '9':'wxyz'}
        ans = ['']
        for k in digits:
            ans = [i+j for i in ans for j in dic[k]]
        return ans

        # 2
        if len(digits)==0: return [] 
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return [''.join(item) for item in itertools.product(*(conversion[char]  for char in digits))]
