from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, dest, w in times:
            adj[source].append((dest, w))
        
        q = []
        heapq.heappush(q, (0, k))
        dist = [float("inf") for i in range(n)]
        dist[k - 1] = 0

        while q:
            cur_w, cur = heapq.heappop(q)
            if dist[cur - 1] < cur_w:
                continue
            
            for neigh, neigh_w in adj[cur]:
                neigh_dist = cur_w + neigh_w
                if dist[neigh - 1] > neigh_dist:
                    dist[neigh - 1] = neigh_dist
                    heapq.heappush(q, (neigh_dist, neigh))
        res = max(dist)
        return res if res != float("inf") else -1
                 