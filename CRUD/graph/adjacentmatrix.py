class graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adjacent_matrix=[[0]*vno for e in range(vno)]
    def add_edge(self,u,v,weight=1):
        if self.vertex_count>u>=0 and self.vertex_count>v>=0:
            self.adjacent_matrix[u][v]=weight
            self.adjacent_matrix[v][u]=weight
        else:
            print('invalid vertex')
    def remove_edge(self,u,v):
        if self.vertex_count>u>=0 and self.vertex_count>v>=0:
            self.adjacent_matrix[u][v]=0
            self.adjacent_matrix[v][u]=0
        else:
            print('invalid vertex')
    def has_edge(self,u,v):
        if self.vertex_count>u>=0 and self.vertex_count>v>=0:
            return self.adjacent_matrix[u][v]!=0
        else:
            print('invalid vertex')
    def print_matrix(self):
        for rowlist in self.adjacent_matrix:
            l=map(str,rowlist)
            print(' '.join(l))