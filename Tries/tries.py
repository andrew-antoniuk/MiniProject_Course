"""
Docstring for Tries.tries
"""

class TrieNode:

    """
    Node for Trie Tree ADT
    """

    def __init__(self, letter):
        self.letter = letter
        self.children = [None] * 26
        self.is_leaf = False

    def __eq__(self, other):
        return self.letter == other.letter

class TrieADT:

    """
    Trie Tree ADT
    """

    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):

        """
        Add new word to the Trie ADT
        """

        node = self.root
        for ch in word.lower():
            index = ord(ch) - ord("a")
            if node.children[index] is None:
                node.children[index] = TrieNode(ch)
            node = node.children[index]
        node.is_leaf = True

    def is_empty(self):

        """
        No children for initial node
        """

        return all(n is None for n in self.root.children)

    def search(self, word: str) -> bool:

        """
        Docstring for search
        """

        node = self.root
        for ch in word.lower():
            index = ord(ch) - ord("a")
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.is_leaf

    def startswith(self, prefix: str):

        """
        Find the node that starts with this prefix
        """

        node = self.root
        for ch in prefix:
            index = ord(ch) - ord("a")
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

class WordDict:

    """
    Word Dictionary based on Tree ADT
    """

    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):

        """
        Add new word to the Trie ADT
        """

        node = self.root
        for ch in word.lower():
            index = ord(ch) - ord("a")
            if node.children[index] is None:
                node.children[index] = TrieNode(ch)
            node = node.children[index]
        node.is_leaf = True

    def is_empty(self):

        """
        No children for initial node
        """

        return all(n is None for n in self.root.children)

    def search(self, word: str) -> bool:

        """
        Docstring for search
        """

        def dfs(node: TrieNode, i):
            if i == len(word):
                return node.is_leaf

            if word[i] == ".":
                for ch in node.children:
                    if dfs(ch.letter, i + 1):
                        return True
                return False
            if TrieNode(word[i]) in node.children:
                return dfs(node.children[ord(word[i]) - ord("a")], i + 1)
            return False

        return dfs(self.root, 0)
