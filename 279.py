#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：279题  给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
作者：ithh
时间：Fri Sep  4 11:17:11 2020
"""

class Solution:
    # 任何一个正整数都可以表示成不超过四个整数的平方之和。拉格朗日4数定理 
    # 推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=4^a(8b+7)
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        
        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return bool(a) + bool(b)
            a += 1
        
        return 3

class Solution1:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n+1):
            dp.append(min(dp[-j*j] for j in range(1, 1 + int(i**0.5))) + 1)
        return dp[-1]



from queue import Queue

class Solution2:
    def numSquares(self, n: int) -> int:
        around = []
        for i in range(1, n + 1):
            if i**2 <= n:
                around.append(i**2)
            else:
                break
        
        r = 0
        seen = set() # 防止重复运算
        
        # ----------------BFS 开始----------------------
        # 初始化根节点
        q = Queue()
        q.put((0, r))
        
        # 进入队列循环
        while not q.empty():
            # 取出一个元素
            cur, step = q.get()
            step += 1
            
            # 放入周围元素
            for a in around:
                a += cur
                if a == n:
                    return step
                if a < n and (a, step) not in seen:
                    seen.add((a, step))
                    q.put((a, step))
        # ----------------------------------------------
        return 0




class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)


class Solution3:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1,int(vertex.value**.5)+1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i==0:                   
                    return new_vertex.step
                    
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
                                        
        return -1
