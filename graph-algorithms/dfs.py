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