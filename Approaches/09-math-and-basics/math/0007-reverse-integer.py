# 7. Reverse Integer  [Medium]
# https://leetcode.com/problems/reverse-integer/
# runtime 35 ms | memory 18 MB

class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        if x == 0 :
           a=0
        elif x < 0:
            x = x * (-1)
            temp = 0
            while x > 0:
                temp = temp * 10
                temp = temp + (x % 10)
                x = int(x / 10)
            temp = temp * (-1)
            if(temp < -2147483648):
             a = 0
            else:
             a=temp    
        elif x > 0 :
            temp = 0
            while x > 0:
                temp = temp * 10
                temp = temp + (x % 10)
                x = int(x / 10)
            if(temp > 2147483647):
             a = 0
            else:
             a=temp
        return a
