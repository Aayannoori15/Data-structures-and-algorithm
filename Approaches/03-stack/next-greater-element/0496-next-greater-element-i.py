# 496. Next Greater Element I  [Easy]
# https://leetcode.com/problems/next-greater-element-i/
# runtime 19 ms | memory 19.3 MB

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono=[]
        ans=[]
        for i in range(-1,-len(nums2)-1,-1):
            if not mono:
                ans.append(-1)
            elif nums2[i]>mono[-1]:
                while mono and nums2[i]>=mono[-1]:
                    mono.pop()
                if mono:
                    ans.append(mono[-1])
                else:
                    ans.append(-1)
            else:
                ans.append(mono[-1])
            mono.append(nums2[i])
        ans.reverse()
        f=[]
        for i in nums1:
            idx=nums2.index(i)
            f.append(ans[idx])
        return f
