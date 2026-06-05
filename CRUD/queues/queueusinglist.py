class queue:
    def __init__(self):
        self.item=[]
        self.front=None 
        self.rear=None 
    def is_empty(self):
        return len(self.item)==0
    def enqueue(self,data):
        if self.is_empty():
            self.item.append(data)
            self.front=self.item[0]
        else:
            self.item.append(data)
        self.rear=self.item[-1]
    def dequeue(self):
        if self.is_empty():
            raise Exception('queue underflow')
        elif len(self.item) == 1:
            self.item.pop(0) 
            self.front=None
            self.rear=None
        else: 
            self.item.pop(0)
            self.front=self.item[0]
            self.rear = self.item[-1]
    def get_front(self):
        if self.is_empty():
            raise Exception('no element in queue')
        else:
            return self.front
    def get_rear(self):
        if self.is_empty():
            raise Exception('no element in queue')
        else:
            return self.rear
    def get_size(self):
        return len(self.item)     
    def show_queue(self):
        print(self.item)  