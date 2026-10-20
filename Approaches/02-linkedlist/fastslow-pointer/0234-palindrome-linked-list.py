# 234. Palindrome Linked List  [Easy]
# https://leetcode.com/problems/palindrome-linked-list/
# runtime 860 ms | memory 53.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val=[]
        s=''
        b=''
        while head:
            val.append(head.val)
            head=head.next
        for i in val:
            s=s+str(i)
            b=str(i)+b
        if b==s:
            return True 
        return False
