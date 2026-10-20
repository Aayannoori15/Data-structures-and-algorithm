# 605. Can Place Flowers  [Easy]
# https://leetcode.com/problems/can-place-flowers/
# runtime 7 ms | memory 18 MB

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=1
        if len(flowerbed) >= 2:
            if flowerbed[1]==0 and flowerbed[0] ==0:
                flowerbed[0]=2
            if flowerbed[-1]==0 and flowerbed[-2] ==0:
                flowerbed[-1]=2
        while i < len(flowerbed)-1:
            if flowerbed[i]==0:
                if flowerbed[i-1]==0 and  flowerbed[i+1]==0:
                    flowerbed[i]=2
                    i+=2
                else:
                    i+=1
            else:
                 i+=1
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n <= 1
        if flowerbed.count(2)>=n:
            return True
        else:
            return False
