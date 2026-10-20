# 141. Linked List Cycle  [Easy]
# https://leetcode.com/problems/linked-list-cycle/
# runtime 55 ms | memory 22.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False 
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True 
        return False
