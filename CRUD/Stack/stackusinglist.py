class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.isempty() is not True:
            self.items.pop()
        else:
            raise StopIteration('its empty')
    def peak(self):
        if self.isempty() is not True:
            self.items[-1]
        else:
            print('stack is empty')
    def size(self):
        return len(self.items)
    