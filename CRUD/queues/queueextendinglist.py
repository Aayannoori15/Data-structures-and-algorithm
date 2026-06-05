class queue(list):
    def is_empty(self):
        return len(self)==0
    def dequeue(self):
        if not self.is_empty():
            val=self[0]
            print(val)
            self.pop(0)
        else:
            raise IndexError('no element is queue')
    def enqueue(self,data):
        self.append(data)
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise Exception('no elements')
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise Exception('no elements')
    def get_size(self):
        return len(self)