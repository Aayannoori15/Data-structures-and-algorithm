# 501. Find Mode in Binary Search Tree  [Easy]
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# runtime 1357 ms | memory 22.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root,l):
            if not root:
                return 
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            return l
        l=inorder(root,l)
        new=[]
        for i in range(len(l)):
            c=l.count(l[i])
            new.append((c))
        max_val=max(new)
        ans=[]
        for i in range(len(new)):
            if new[i]==max_val:
                ans.append(l[i])
        return list(set(ans))
