class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {u: [] for word in words for u in word}

        for i in range(n - 1):
            word_1, word_2 = words[i], words[i + 1]
            min_len = min(len(word_1), len(word_2))
            if len(word_1) > len(word_2) and word_1[:min_len] == word_2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word_1[j] != word_2[j]:
                    adj[word_1[j]].append(word_2[j])
                    break
        visited = {}
        res = []

        def dfs(u: str):
            if u in visited:
                return visited[u]
            
            visited[u] = True

            for v in adj[u]:
                print("n", v)
                if dfs(v):
                    return True
            
            visited[u] = False
            res.append(u)
            return False
        
        for u in adj:
            print(u)
            if dfs(u):
                return ""

        res.reverse()
        return "".join(res)