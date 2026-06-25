from collections import defaultdict

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        mp = defaultdict(list)

        for i in range(n):
            mp[ratings[i]].append(i)
        
        keys = sorted(mp.keys())

        for key in keys:
            for i in mp[key]:
                max_candy = candy[i]
                if i > 0 and ratings[i] > ratings[i - 1]:
                    max_candy = max(max_candy, candy[i - 1] + 1)
                if i < n - 1 and ratings[i] > ratings[i + 1]:
                    max_candy = max(max_candy, candy[i + 1] + 1)
                candy[i] = max_candy
        return sum(candy)
        