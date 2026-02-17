'''
104 Maximum depth of binary tree
'''

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

if __name__ == "__main__":
    '[1,null,2]'
    node1 = TreeNode(1)
    node1.left = TreeNode('null')
    node1.right = TreeNode('2')

    s = Solution()
    print(s.maxDepth(node1))
