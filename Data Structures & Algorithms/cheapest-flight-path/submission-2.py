import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, c in flights:
            adj_list[u].append((v, c))
        INF = float("inf")
        dist = [[INF] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        q = [(0, src, -1)]
        while q:
            cost, u, step = heapq.heappop(q)
            
            if u == dst:
                return cost
            
            if step == k or dist[u][step + 1] < cost:
                continue
            
            for v, c in adj_list[u]:
                new_step = step + 1
                new_cost = cost + c
                if dist[v][new_step + 1] > new_cost:
                    dist[v][new_step + 1] = new_cost
                    heapq.heappush(q, (new_cost, v, new_step))

        return -1
                
            
