# 374. Guess Number Higher or Lower  [Easy]
# https://leetcode.com/problems/guess-number-higher-or-lower/
# runtime 34 ms | memory 19.1 MB

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while l <= h:
            m = (l + h) // 2
            x = guess(m)
            if x == 0:
                return m
            elif x == -1:
                h = m - 1
            else:
                l = m + 1
