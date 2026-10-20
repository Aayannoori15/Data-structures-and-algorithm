# 1071. Greatest Common Divisor of Strings  [Easy]
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# runtime 3 ms | memory 17.8 MB

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 1
        ans = ""
        if str1 + str2 != str2 + str1:
            return ""
        else:
            s3 = str1 + str2
            while i <= len(str2):  # use str2 as the shorter limit
                if s3[0:i] * (len(str1) // i) == str1 and s3[0:i] * (len(str2) // i) == str2:
                    if len(str1) % i == 0 and len(str2) % i == 0:
                        ans = s3[0:i]
                i += 1
        return ans
