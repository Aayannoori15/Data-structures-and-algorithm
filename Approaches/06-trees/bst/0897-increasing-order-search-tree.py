# 897. Increasing Order Search Tree  [Easy]
# https://leetcode.com/problems/increasing-order-search-tree/
# runtime 0 ms | memory 19.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root,l):
            if not root:
                return l
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            return l
        arr=inorder(root,[])
        head=TreeNode()
        temp=head
        for i in range(len(arr)):
            temp.val=arr[i]
            if i!=len(arr)-1:
                new_node=TreeNode()
                temp.right=new_node
                temp.left=None
                temp=new_node
        return head
