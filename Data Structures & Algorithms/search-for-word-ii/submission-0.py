class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.count = 0
    
    def add(self, word, idx):
        cur = self
        cur.count += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.count += 1
        cur.idx = idx


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.add(words[i], i)
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            if (
                r < 0 or
                c < 0 or
                r >= ROWS or
                c >= COLS or
                board[r][c] == "*" or
                not node.children.get(board[r][c])
            ):
                return
            
            tmp = board[r][c]
            board[r][c] = "*"
            prev = node
            node = node.children[tmp]

            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.count -= 1
                if node.count == 0:
                    prev.children[tmp] = None
                    del node
                    board[r][c] = tmp
                    return
            
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(r + dx, c + dy, node)
            
            board[r][c] = tmp

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        
        return res