# 23. Merge k Sorted Lists  [Hard]
# https://leetcode.com/problems/merge-k-sorted-lists/
# runtime 8 ms | memory 23 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        s=[] 
        for i in lists:
            while i:
                s.append(i.val)
                i=i.next
        s.sort()
        def createLL(arr):
            dummy = ListNode()
            curr = dummy
            for x in arr:
                curr.next = ListNode(x)
                curr = curr.next
            return dummy.next
        return  createLL(s)
