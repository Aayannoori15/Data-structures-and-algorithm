# 2352. Equal Row and Column Pairs  [Medium]
# https://leetcode.com/problems/equal-row-and-column-pairs/
# runtime 22 ms | memory 24.7 MB

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_set=[]
        for i in range(len(grid)):
            ap=[]
            for j in range(len(grid)):
                ap.append(grid[j][i])
            col_set.append(ap)
        col_set = [tuple(x) for x in col_set]
        grid = [tuple(x) for x in grid]
        c=0
        dict1={}
        dict2={}
        for i in col_set:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in grid:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        for i in dict1:
            if i in dict2:
                c += dict1[i] * dict2[i]
        return c
