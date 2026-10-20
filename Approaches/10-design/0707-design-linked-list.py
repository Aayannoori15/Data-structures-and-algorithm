# 707. Design Linked List  [Medium]
# https://leetcode.com/problems/design-linked-list/
# runtime 77 ms | memory 18.5 MB

class Node:
    def __init__(self,item,next):
        self.item=item
        self.next=next

class MyLinkedList:
    def __init__(self,start=None):
        self.start=start
        

    def get(self, index: int) -> int:
        count=0
        head=self.start
        while head:
            if count==index:
                return head.item
            else:
                count+=1
                head=head.next
        return -1

    def addAtHead(self, val: int) -> None:
        n=Node(val,self.start)
        self.start=n
        

    def addAtTail(self, val: int) -> None:
        if not self.start:
            self.start = Node(val, None)
            return
        head=self.start
        while head.next:
            head=head.next
        n=Node(val,None)
        head.next=n

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        count=0
        head=self.start
        while head:
            if count==index-1:
                n=Node(val,head.next)
                head.next=n
                return
            else:
                count+=1
                head=head.next
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.start:
            return
        if index == 0:
            self.start = self.start.next
            return
        count=0
        head=self.start
        while head:
            if count==index-1 and head.next:
                head.next=head.next.next
                return
            else:
                count+=1
                head=head.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
