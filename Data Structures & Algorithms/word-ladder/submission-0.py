from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        n, m = len(wordList), len(wordList[0])
        mp = {wordList[i]: i for i in range(n)}

        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        cnt += 1
                if cnt == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        
        q, res = deque(), 1
        visit = set()
        
        for i in range(m):
            for c in range(ord("a"), ord("z") + 1):
                if chr(c) == beginWord[i]:
                    continue
                word = beginWord[:i] + chr(c) + beginWord[i + 1:]
                if word in mp and mp[word] not in visit:
                    q.append(mp[word])
                    visit.add(mp[word])

        while q:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if wordList[node] == endWord:
                    return res
                for nei in adj_list[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        return 0    
        

        