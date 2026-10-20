# 102. Binary Tree Level Order Traversal  [Medium]
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# runtime 2 ms | memory 20.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([])
        def bst(root,queue):
            l=[]
            a=[]
            if not root:
                return l
            queue.append(root)
            while queue:
                size=len(queue)
                while size!=0:
                    node=queue.popleft()
                    if node is not None:
                        a.append(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                        size-=1
                l.append(a)
                a=[]
            return l
        return bst(root,queue)
