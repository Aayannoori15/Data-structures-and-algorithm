class stack(list):
    def isempty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if self.isempty() is not True:
            super().pop()
        else:
            print('stack empty')
    def peak(self):
        return self[-1]
    def size(self):
        return len(self)
    """overiding functions """
    def insert(self,data,index):
        raise AttributeError