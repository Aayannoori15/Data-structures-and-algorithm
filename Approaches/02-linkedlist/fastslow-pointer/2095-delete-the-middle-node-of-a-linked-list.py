# 2095. Delete the Middle Node of a Linked List  [Medium]
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# runtime 59 ms | memory 49.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head
