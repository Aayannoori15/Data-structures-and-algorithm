# 92. Reverse Linked List II  [Medium]
# https://leetcode.com/problems/reverse-linked-list-ii/
# runtime 0 ms | memory 17.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        leftnode=dummy
        rightnode=dummy
        for i in range(left - 1):
            leftnode = leftnode.next
        reverse = leftnode.next
        rightnode = reverse
        for i in range(right - left):
            rightnode = rightnode.next
        r = rightnode.next
        prev=None
        current=reverse 
        while current is not r:
            nxt=current.next 
            current.next=prev
            prev=current 
            current=nxt 
        leftnode.next=prev
        reverse.next=r 
        return dummy.next
