"""
Docstring for Trees.trees
"""

from collections import deque

class BinaryTreeNode:

    """
    Docstring for BinaryTreeNode
    """

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.value == other.value
        # return self.value == other.value and self.left == other.left and self.right == other.right

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

    def add(self, value):

        """
        Docstring for append
        """

        new = BinaryTreeNode(value)

        if self.empty():
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

    def empty(self) -> bool:

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

        if self.empty():
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

    def invert_recursive(self):

        """
        Swap children of each subtree in the tree with recursion
        """

        self._invert_helper(self.root)

    def _invert_helper(self, node):

        """
        The actual recursive logic
        Preserves the method above from crashes and occasional errors
        And gives better understanding of the logic
        """

        if node is None:
            return

        node.left, node.right = node.right, node.left

        self._invert_helper(node.left)
        self._invert_helper(node.right)

    def depth(self):

        """
        Maximum depth of the tree
        """

        return self._depth_helper(self.root)

    def _depth_helper(self, root):

        """
        Helper for depth method
        """

        if not root:
            return 0

        return 1 + max(self._depth_helper(root.left), self._depth_helper(root.right))

    def max_depth(self):

        """
        Maximum depth
        """

        if self.empty():
            return 0

        depth = 0
        queue = deque([self.root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth

    def depth_stack(self):

        """
        Depth
        """

        if self.empty():
            return 0

        max_depth = 0
        stack = deque([(self.root, 1)])
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth

    def node_depth(self, node):

        """
        Depth of a specific node from this tree
        """

        if self.empty():
            return -1

        depth = -1
        queue = deque([self.root])
        while queue:
            temp = deque()
            for n in queue:
                left, right = n.left, n.right

                if left:
                    if left is node:
                        return depth
                    temp.append(left)

                if right:
                    if right is node:
                        return right
                    temp.append(right)

            queue = temp
            depth += 1

        return depth

    def bfs(self):

        """
        BFS
        """

        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            result.append(current.value)

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

    def is_same_tree(self, other) -> bool:

        """
        Verify if the tree is the same as current
        """

        if self.empty() and other.empty():
            return True

        if self.empty() or other.empty():
            return False

        queue = deque([(self.root, other.root)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True

    def is_same_tree_rec(self, other) -> bool:

        """
        Docstring for is_same_tree_rec
        """

        return self._is_same_tree_rec_helper(self.root, other.root)

    def _is_same_tree_rec_helper(self, tree1, tree2):

        """
        Docstring for is_same_tree_rec_helper
        """

        if tree1 is None and tree2 is None:
            return True

        if tree1 is None or tree2 is None or tree1 != tree2:
            return False

        left = self._is_same_tree_rec_helper(tree1.left, tree2.left)
        right = self._is_same_tree_rec_helper(tree1.right, tree2.right)

        return left and right

    # def is_subtree(self, tree):

    #     """
    #     Is that tree a subtree of this one
    #     """

    #     if tree.empty():
    #         return True

    #     if self.empty() and not tree.empty(): # other.root is not None
    #         return False

    #     left = self.is_subtree()
