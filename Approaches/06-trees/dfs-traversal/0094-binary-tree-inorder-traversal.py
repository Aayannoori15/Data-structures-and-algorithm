# 94. Binary Tree Inorder Traversal  [Easy]
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# runtime 0 ms | memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root,l):
            if not root:
                return 
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            return l 
        l=inorder(root,l)
        if not l:
            return []
        return l
