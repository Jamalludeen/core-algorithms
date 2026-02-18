class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            self._insert_node(data, self.root)
        else:
            self.root = Node(data=data, parent=None)
    
    def _insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self._insert_node(data, node.left_node)
            else:
                node.left_node = Node(data=data, parent=node)
        else:
            if node.right_node:
                self._insert_node(data, node.right_node)
            else:
                node.right_node = Node(data=data, parent=node)

    def in_order(self):
        if self.root:
            self._in_order_traversal(self.root)
        else:
            print("Tree is empty")
    
    def _in_order_traversal(self, node):
        if node.left_node:
            self._in_order_traversal(node.left_node)
        print(node.data)

        if node.right_node:
            self._in_order_traversal(node.right_node)

def dfs_tree_traversal(tree, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node.data, end=' ')
        visited.add(node.data)
        if node.left_node:
            dfs_tree_traversal(tree=tree, node=node.left_node, visited=visited)
        if node.right_node:
            dfs_tree_traversal(tree=tree, node=node.right_node, visited=visited)


if __name__ == "__main__":
    binaryTree = BinaryTree()
    binaryTree.insert(8)
    binaryTree.insert(4)
    binaryTree.insert(12)
    binaryTree.insert(2)
    binaryTree.insert(6)
    binaryTree.insert(10)
    binaryTree.insert(14)
    dfs_tree_traversal(tree=binaryTree, node=binaryTree.root)