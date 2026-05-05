"""
Docstring for Tries.tries
"""

class TrieNode:

    """
    Docstring for TrieNode
    """

    def __init__(self, letter):
        self.letter = letter
        self.children = [None] * 26
        self.is_leaf = False

class TrieADT:

    """
    Docstring for TrieADT
    """

    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):

        """
        Add new word to the Trie ADT
        """

        current = self.root
        for letter in word.lower():
            index = ord(letter) - ord("a")
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
            current = current.children[index]
        current.is_leaf = True

    def is_empty(self):

        """
        No children for initial node
        """

        return all(n is None for n in self.root.children)

    def search(self, word: str) -> bool:

        """
        Docstring for search
        """

        current = self.root
        for letter in word.lower():
            index = ord(letter) - ord("a")
            if not current.children[index]:
                return False
            current = current.children[index]
        return current.is_leaf
