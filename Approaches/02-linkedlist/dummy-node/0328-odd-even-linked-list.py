# 328. Odd Even Linked List  [Medium]
# https://leetcode.com/problems/odd-even-linked-list/
# runtime 0 ms | memory 19.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy2=ListNode(0)
        odd=dummy
        even=dummy2
        count=1
        while head:
            temp=head.next
            if count%2!=0:
                odd.next=head
                odd=odd.next
                odd.next=None
                count+=1
            else:
                even.next=head
                even=even.next
                even.next=None
                count+=1
            head=temp
        odd.next=dummy2.next
        return dummy.next
