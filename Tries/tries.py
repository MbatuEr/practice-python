from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def has_prefix(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def find_all_words_on_a_board(self, board: List[List[str]],
                                  words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        res = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    self.dfs(board, r, c, root.children[board[r][c]], res)
        return res

    def dfs(self, board: List[List[str]], r: int, c: int,
            node: TrieNode, res: List[str]) -> None:
        if node.word:
            res.append(node.word)
            node.word = None
        temp = board[r][c]
        board[r][c] = "#"
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in dirs:
            next_r, next_c = r+ d[0], c + d[1]
            if (self.is_within_bounds(next_r, next_c, board) and 
                board[next_r][next_c] in node.children):
                self.dfs(
                    board, next_r, next_c, 
                    node.children[board[next_r][next_c]],
                    res
                )
        board[r][c] = temp
    
    @staticmethod
    def is_within_bounds(r: int, c: int, board: List[str]) -> bool:
        return 0 <= r < len(board) and 0 <= c < len(board[0])