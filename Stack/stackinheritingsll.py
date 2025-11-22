from linkedlist.Linkedlist import *
class stack(SLL):
    def __init__(self):
        super().__init__(self)
        self.count=0
    def isempty():
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        count+=1
    def pop(self):
        self.deletefirst()
        count-=1
    def peek(self):
        if not self.isempty():
            return self.start.item
        else:
            raise IndexError
    def size(self):
        return self.count