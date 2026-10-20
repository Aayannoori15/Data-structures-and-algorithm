# 2130. Maximum Twin Sum of a Linked List  [Medium]
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# runtime 64 ms | memory 41.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sum=0
        if head==None or head.next==None:
            return head
        else :
            prev=None
            slow =head
            fast=head
            while fast!=None and fast.next!=None:
                prev=slow
                slow= slow.next
                fast=fast.next.next
            prev.next=None
        head1=None
        while slow:
            curr=slow
            slow=slow.next
            curr.next=head1
            head1=curr
        while head1 and head:
            temp=head.next
            temp1=head1.next
            if (head.val+head1.val)>=sum:
                sum=(head.val+head1.val)
            head=temp
            head1=temp1
        return sum
