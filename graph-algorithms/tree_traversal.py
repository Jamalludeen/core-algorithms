from collections import deque


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

    def pre_order(self):
        if self.root:
            self._pre_order_traversal(self.root)
        else:
            print("Tree is empty")

    def _pre_order_traversal(self, node):
        print(node.data)
        if node.left_node:
            self._pre_order_traversal(node.left_node)
        if node.right_node:
            self._pre_order_traversal(node.right_node)

    def post_order(self):
        if self.root:
            self._post_order_traversal(self.root)
        else:
            print("Tree is empty")

    def _post_order_traversal(self, node):
        if node.left_node:
            self._post_order_traversal(node.left_node)
        if node.right_node:
            self._post_order_traversal(node.right_node)
        print(node.data)

    def level_order(self):
        if not self.root:
            print("Tree is empty")
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data)
            if node.left_node:
                queue.append(node.left_node)
            if node.right_node:
                queue.append(node.right_node)

    def search(self, data):
        return self._search_node(data, self.root)

    def _search_node(self, data, node):
        if node is None:
            return None
        if data == node.data:
            return node
        if data < node.data:
            return self._search_node(data, node.left_node)
        return self._search_node(data, node.right_node)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left_node), self._height(node.right_node))

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left_node) + self._count_nodes(node.right_node)

def dfs_tree_traversal(tree, node, visited=None):
    if visited is None:
        visited = set()
    
    if node.data not in visited:
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