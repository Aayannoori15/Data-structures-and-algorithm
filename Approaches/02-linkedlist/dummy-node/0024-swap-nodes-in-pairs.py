# 24. Swap Nodes in Pairs  [Medium]
# https://leetcode.com/problems/swap-nodes-in-pairs/
# runtime 0 ms | memory 17.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head 
        while dummy:
            if dummy.next is not None:
                dummy.val,dummy.next.val=dummy.next.val,dummy.val
                dummy=dummy.next.next
            else:
                break
        return head
