# 21. Merge Two Sorted Lists  [Easy]
# https://leetcode.com/problems/merge-two-sorted-lists/
# runtime 0 ms | memory 17.6 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        head=dummy
        while list1 and list2:
            temp=list1.next
            temp2=list2.next
            if list1.val<=list2.val:
                dummy.next=list1
                list1=temp
                dummy=dummy.next
            else:
                dummy.next=list2
                list2=temp2
                dummy=dummy.next
        if list1:
            dummy.next=list1
        else:
            dummy.next=list2
        return head.next
