# 1431. Kids With the Greatest Number of Candies  [Easy]
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# runtime 0 ms | memory 17.8 MB

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=0
        result=[]
        for i in candies:
            if i>=max:
                max=i
            else:
                continue
        for i in candies:
            if i + extraCandies >= max:
                 result.append(True)
            else:
                 result.append(False)
        return result
