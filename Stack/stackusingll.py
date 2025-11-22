class node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class stack:
    def __init__(self):
        self.top=None
        self.itemcount=0
    def isempty(self):
        return self.itemcount==0
    def push(self,data):
        n=node(data)
        self.top=n(data,self.top)
        self.top=n
        itemcount+=1
    def pop(self):
        if self.isempty() is not True:
            data=self.top.val
            self.top=self.top.next
            itemcount-=1
            return data
        else:
            raise IndexError('stack empty')
    def peak(self):
        if self.isempty() is not True:
            return self.top.val
        else:
            raise IndexError('stack empty')
    def size(self):
        return self.itemcount