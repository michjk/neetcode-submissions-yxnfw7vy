class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        return self._search(word, 0)

    def _search(self, word: str, pos: int) -> bool:
        if pos == len(word):
            return self.is_word
        
        if word[pos] == ".":
            if not self.children:
                return False
            return any(child._search(word, pos + 1) for child in self.children.values())
        
        if word[pos] in self.children:
            return self.children[word[pos]]._search(word, pos + 1)
        
        return False
