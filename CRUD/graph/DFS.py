def dfs(graph,start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()  
        if node not in visited:
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)