def dfs(root):
    if not root:
        return 
    stack=[root]
    if stack:
        node=stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)