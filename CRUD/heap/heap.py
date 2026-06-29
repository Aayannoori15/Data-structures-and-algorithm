class EmptyHeapException(Exception):
    def __init__(self,msg='emptyheap'):
        self.msg=msg
    def __str__(self):
        return self.msg
class heap:
    def __init__(self):
        self.heap=[]
    def createheap(self,list1):
        for e in list1:
            self.insert(e)
    def insert(self,e):
        index=len(self.heap)
        parentindex=(index-1)//2
        while index>0 and self.heap[parentindex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentindex])
            else:
                self.heap[index]=self.heap[parentindex]
            index=parentindex
            parentindex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            return self.heap.pop()
        max_val=self.heap[0]
        temp=self.heap.pop()
        index=0
        left=(index*2)+1
        right=(index*2)+2
        while left<len(self.heap):
            if right<len(self.heap):
                if self.heap[left]>self.heap[right]:
                    if self.heap[left]>temp:
                        self.heap[index]=self.heap[left]
                        index=left 
                    else:
                        break
                else:
                    if self.heap[right]>temp:
                        self.heap[index]=self.heap[right]
                        index=right
                    else:
                        break
            else:
                if self.heap[left]>temp:
                    self.heap[index]=self.heap[left]
                    index=left
                else:
                    break
            left=(index*2)+1
            right=(index*2)+2
        self.heap[index]=temp
        return max_val
    def heap_sort(self,list1):
        self.createheap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2

