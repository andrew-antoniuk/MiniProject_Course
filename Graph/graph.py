"""
Docstring for Graph.graph
"""

from collections import deque

class Node:

    """
    Docstring for Node
    """

    def __init__(self, value = 0):
        self.value = value
        self.neighbors = []

    def __bool__(self) -> bool:
        return self.value is not None

    def __eq__(self, other) -> bool:
        return self.value == other.value

class NodeAdj:

    """
    Graph Node
    """

    def __init__(self, value, coords: tuple = None):
        self.value = value
        self.coords = coords

    def __eq__(self, other):
        return self.coords == other.coords

class GraphAdj:

    """
    Adjacency graph build by linking neighbouring nodes
    """

    def __init__(self):
        self.nodes: dict[NodeAdj, dict] = {}

    def add(self, node: NodeAdj):

        """
        Add new node
        """

        if node in self.nodes:
            return

        connected = []
        y, x = node.coords

        for n in list(self.nodes):
            yn, xn = n.coords

            is_adj = (
                (abs(y - yn) == 1 and x == xn) or
                (abs(x - xn) == 1 and y == yn)
            )


            if is_adj:

                self.nodes[n].append(node)
                connected.append(n)

        self.nodes[node] = connected

    def empty(self):

        """
        Check if the graph is empty
        """

        return not self.nodes

def island_count(grid) -> int:

    """
    Docstring for island_count
    """

    if not grid:
        return 0

    def dfs(y, x):
        if (y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] == "0"):
            return

        grid[y][x] = "0"
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1

    return count

def clone_graph(node: Node) -> Node:

    """
    Docstring for clone_graph
    """

    if not node:
        return None

    clonned = {}
    clonned[node] = Node(node.value)
    queue = deque([node])

    while queue:
        current = queue.popleft()
        for n in current.neighbors:
            if n not in clonned:
                clonned[n] = Node(n.value)
                queue.append(n)
            clonned[current].neighbors.append(clonned[n])

    return clonned[node]
