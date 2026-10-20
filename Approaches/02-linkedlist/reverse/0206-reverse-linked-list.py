# 206. Reverse Linked List  [Easy]
# https://leetcode.com/problems/reverse-linked-list/
# runtime 0 ms | memory 18.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=None
        while head:
            temp=head.next
            head.next=dummy
            dummy=head
            head=temp
        return dummy
