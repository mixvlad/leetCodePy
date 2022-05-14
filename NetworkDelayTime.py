import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Implement Bellman-Ford algorithm
        weights = [sys.maxsize for i in range(n)]
        weights[k-1] = 0

        for i in range(n):
            for x in times:
                if weights[x[1]-1] > weights[x[0]-1] + x[2]:
                    weights[x[1]-1] = weights[x[0]-1] + x[2]
        res = max(weights)
        if res == sys.maxsize:
            return -1
        return res

    def test(self):
        assert self.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2) == 2
        assert self.networkDelayTime(times = [[1,2,1]], n = 2, k = 1) == 1
        assert self.networkDelayTime(times = [[1,2,1]], n = 2, k = 2) == -1
        
if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        