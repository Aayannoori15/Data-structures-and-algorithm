from linkedlist.Linkedlist import SLL
class stack:
    def __init__(self):
        self.mylist=SLL()
        self.size=0
    def isempty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        size+=1
    def pop(self):
        if not self.isempty():
            self.mylist.deletefirst()
            size-=1
        else:
            raise IndexError
    def peek(self):
         if not self.isempty():
            return self.mylist.start.item
    def size(self):
        return self.size 