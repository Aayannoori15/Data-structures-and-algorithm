# 872. Leaf-Similar Trees  [Easy]
# https://leetcode.com/problems/leaf-similar-trees/
# runtime 0 ms | memory 19.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def kuch(root,l):
            if not root:
                return l
            if root.left is None and root.right is None:
                l.append(root.val)
                return l     
            kuch(root.left,l)
            kuch(root.right,l)
            return l
        l1=[]
        l2=[]
        l1=kuch(root1,l1)
        l2=kuch(root2,l2)
        return l1==l2
