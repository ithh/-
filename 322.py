
#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
功能：题号322
作者：ithh
时间：Thu Aug 27 13:33:08 2020
"""

# 1欧拉通路
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for from_, to_ in tickets:
            if from_ not in graph:
                graph[from_] = {to_:1}
            elif to_ in graph[from_]:
                graph[from_][to_] += 1
            else:
                graph[from_][to_] = 1
        
        for key in graph:
            values = sorted(graph[key].items())
            new_values = []
            for val, num in values:
                for i in range(num):
                    new_values.append((val, i))
            graph[key] = new_values
        
        self.visited = {}
        self.res = []
        def dfs(pla, e):   
            if pla not in self.visited:
                self.visited[pla] = set()
            
            if len(e) >= len(tickets):
                self.res = e
            
            if pla in graph and len(self.res) == 0:
                for (target, num) in graph[pla]:
                    if (target, num) in self.visited[pla]:
                        continue
                    self.visited[pla].add((target, num))
                    if len(e) == len(tickets) - 1:
                        dfs(target, e + [pla, target])
                    else:
                        dfs(target, e + [pla])
                    self.visited[pla].remove((target, num))
            
        dfs('JFK', [])
        return self.res

# 2 DFS
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(node):
            while dic[node]:
                dfs(dic[node].pop())
            res.append(node)           
       
        dic = collections.defaultdict(list)
        for i, j in sorted(tickets)[::-1]:
            dic[i].append(j)
        res = []
        dfs('JFK')
        return res[::-1]
