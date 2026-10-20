# 783. Minimum Distance Between BST Nodes  [Easy]
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# runtime 0 ms | memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result=[]
        def inorder(root,l):
            if not root:
                return l
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            return l
        result=inorder(root,result)
        min_diff=float('inf')
        for i in range(len(result)-1):
            if result[i+1]-result[i]<min_diff:
                min_diff=result[i+1]-result[i]
            if min_diff==1:
                return 1
        return min_diff
