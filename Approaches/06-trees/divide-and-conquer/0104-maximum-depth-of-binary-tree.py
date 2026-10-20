# 104. Maximum Depth of Binary Tree  [Easy]
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# runtime 0 ms | memory 20.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth=1
        stack=[(root,depth)]
        stack2=[(root,depth)]
        while stack:
            node=stack.pop()
            if node:
                if node[0].left:
                    stack.append((node[0].left,node[1]+1))
                    stack2.append((node[0].left,node[1]+1))
                if node[0].right:
                    stack.append((node[0].right,node[1]+1))
                    stack2.append((node[0].right,node[1]+1))
        max_val=0
        for i in stack2:
            if i[1]>max_val:
                max_val=i[1]
        return max_val
