def dfs_iterative(root):
    """
    Iterative DFS traversal using explicit stack

    Args:
        root: Root of the tree

    Returns:
        List of node values in DFS order
    """
    if not root:
        return []

    result = []
    stack = [root]  # Initialize stack with root

    while stack:
        # Pop from stack (LIFO - Last In First Out)
        node = stack.pop()
        result.append(node.val)

        # Push right child first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def dfs_graph(graph, start):
    """
    DFS traversal for graphs (handles cycles)

    Args:
        graph: Adjacency list representation {node: [neighbors]}
        start: Starting node

    Returns:
        List of visited nodes in DFS order
    """
    visited = set()
    result = []

    def dfs(node):
        # Mark current node as visited
        visited.add(node)
        result.append(node)

        # Visit all unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result