# 2300. Successful Pairs of Spells and Potions  [Medium]
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# runtime 710 ms | memory 44.9 MB

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        
        ans=[]
        for spell in spells:
            left=0
            right=len(potions)
            while left < right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid
                else:
                    left = mid + 1
            ans.append(len(potions) - left)
        return ans
