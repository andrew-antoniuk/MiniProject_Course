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

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __repr__(self):
        return f"BinaryTreeNode(value={self.value}, left={self.left}, right={self.right})"

    def __str__(self):
        return f"Node with value {self.value}, left-child {self.left} and right-child {self.right}"

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

    def is_leaf(self, node: BinaryTreeNode) -> bool:

        """
        Leaf status of the node
        """

        return node.left is None and node.right is None

    def is_root(self, node: BinaryTreeNode) -> bool:

        """
        Root status of the node
        """

        return node is self.root

    def invert(self):

        """
        Swap children of each subtree in the tree
        """

        if self.is_empty():
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
