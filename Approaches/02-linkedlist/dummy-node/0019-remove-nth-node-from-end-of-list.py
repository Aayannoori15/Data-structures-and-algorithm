# 19. Remove Nth Node From End of List  [Medium]
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# runtime 0 ms | memory 18 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= head 
        gummy=head
        count=0
        count1=0
        len=0
        #counting nodes 
        while dummy :
            len+=1
            dummy=dummy.next
        count=len-n
        #exceptions
        if head.next==None and n==1:
            return head.next
        if n==1:
            while gummy:
                if gummy.next.next==None:
                    gummy.next=None
                    break
                else:
                    gummy=gummy.next
            return head
        if len==n:
            head=head.next
        #removing nodes 
        else:
            while gummy:
                if count1==count-1 :
                    gummy.next=gummy.next.next
                    break
                else:
                    count1+=1
                    gummy=gummy.next
        return head
