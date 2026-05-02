"""
Docstring for Trees.trees
"""

from collections import deque

class BinaryTreeNode:

    """
    Docstring for BinaryTreeNode
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    """
    Docstring for BinaryTree
    """

    def __init__(self, root = None):
        self.root = root

    def append(self, value):

        """
        Docstring for append
        """

        new = BinaryTreeNode(value)

        if self.is_empty():
            self.root = new
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()

            if node.left is None: # check left
                node.left = new
                return
            queue.append(node.left)

            if node.right is None: # check right
                node.right = new
                return
            queue.append(node.right)

    def is_empty(self) -> bool:

        """
        Docstring for is_empty
        """

        return self.root is None
