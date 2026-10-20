# 450. Delete Node in a BST  [Medium]
# https://leetcode.com/problems/delete-node-in-a-bst/
# runtime 3 ms | memory 22.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(root):
            while root.left:
                root=root.left 
            return root
        if not root:
            return root
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif root.val == key:
            if root.left and root.right:
                n=find_min(root.right)
                root.val=n.val
                root.right=self.deleteNode(root.right,n.val)
                return root
                return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None 
        return root
