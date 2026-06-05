class node:
    def __init__(self,item=None,next=None):
        self.item=item 
        self.next=next 
class deque:
    def __init__(self):
        self.item_count=0
        self.front=None 
        self.rear=None 
    def is_empty(self):
        return self.item_count==0
    def insert_front(self,data):
        n=node(data,self.front)
        if self.item_count==0:
            self.rear=n
        self.front=n
        self.item_count+=1
    def insert_rear(self,data):
        n=node(data)
        if self.item_count==0:
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def delete_front(self):
        if self.item_count==0:
            raise Exception('no elements to delete')
        elif self.item_count==1:
            self.rear=None 
            self.front=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def delete_rear(self):
        if self.item_count==0:
            raise Exception('no elements to delete')
        elif self.item_count==1:
            self.rear=None 
            self.front=None
        else:
            temp=self.front
            while temp.next != self.rear:
                temp=temp.next 
            self.rear=temp
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        return self.front
    def get_rear(self):
        return self.rear 
    def size(self):
        return self.item_count