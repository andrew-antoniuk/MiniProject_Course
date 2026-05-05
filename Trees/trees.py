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

        if self.is_empty():
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

        if self.is_empty():
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

        if self.is_empty():
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

        if self.is_empty() and other.empty():
            return True

        if self.is_empty() or other.empty():
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

class BinarySearchTree:

    """
    Docstring for BinarySearchTree
    """

    def __init__(self, node = None):
        self.root = node

    def is_empty(self) -> bool:

        """
        Emptiness of the BST
        """

        return self.root is None

    def add(self, value):

        """
        Add new node to BST
        """

        new = BinaryTreeNode(value)

        if self.is_empty():
            self.root = new
            return

        parent = None
        current = self.root
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return

        if value < parent.value:
            parent.left = new
        else:
            parent.right = new

    def is_inside(self, value) -> bool:

        """
        Docstring for is_inside
        """

        if self.is_empty():
            return False

        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    def is_root(self, node):

        """
        Check if this node is the root
        """

        return self.root is node

    def find_path_to(self, value):

        """
        Find path to the specific value
        """

        path = []

        if self.is_empty():
            return path

        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
                path.append(current.left.value)
            elif value > current.value:
                current = current.right
                path.append(current.right.value)
            else:
                return path

        return path

    def lca(self, val1, val2):

        """
        Finds lowest common ancestor of 2 nodes
        """

        if self.is_empty():
            return None

        path1, path2 = self.find_path_to(val1), self.find_path_to(val2)
        for i in range(min(len(path1), len(path2)) + 1):
            if path1[i] != path2[i]:
                return self.get_node(path1[i - 1])

        return None

    def get_node(self, value):

        """
        Docstring for get_node
        """

        if self.is_empty():
            return None

        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current

        return None

    def level_order_traversal(self):

        """
        Traverse the Tree with Level Order Traversal
        """

        if self.is_empty():
            return []

        current = self.root
        result, level = [], deque([current])

        while level:
            for _ in range(len(level)):
                n = level.popleft()
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
            result.append(level)

        return result

    # def validate_tree(self):

    #     """
    #     Docstring for validate_tree
    #     """

    #     if self.is_empty():
    #         return True

    #     def helper(root):
    #         if

    #         return helper(root.left) and helper(root.right)
    #     return helper(self.root)
