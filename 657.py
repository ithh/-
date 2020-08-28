
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：657号题 ，判断机器人能否返回原点
作者：ithh
时间：Fri Aug 28 15:39:12 2020
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 1
        # if moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D'):
        #     return True
        # else:
        #     return False
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

        # 2 调用hash表减少内存消耗
        c = Counter(moves)
        return c["U"] == c["D"] and c["L"] == c["R"]

