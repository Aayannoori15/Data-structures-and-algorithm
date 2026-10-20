# 230. Kth Smallest Element in a BST  [Medium]
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# runtime 0 ms | memory 22.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root,l):
            if not root:
                return l 
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            return l
        result=[]
        result=inorder(root,result)
        return result[k-1]
