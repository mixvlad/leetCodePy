from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)

        width = 0
        if height:
            width = len(obstacleGrid[0])
            if obstacleGrid[0][0] == 1:
                return 0
        
        @lru_cache
        def recursive(i: int, j: int):
            res = 0
            if i == height - 1 and  j == width - 1 and obstacleGrid[i][j] == 0:
                return 1
            if i+1 < height and obstacleGrid[i+1][j] == 0:
                res += recursive(i+1, j)
            if j+1 < width and obstacleGrid[i][j+1] == 0:
                res += recursive(i, j+1)
            return res

        return recursive(0, 0)
           
    def test(self):
        assert self.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2
        assert self.uniquePathsWithObstacles([[0,1],[0,0]]) == 1
        assert self.uniquePathsWithObstacles([[1]]) == 0
        assert self.uniquePathsWithObstacles([[0,1]]) == 0
        assert self.uniquePathsWithObstacles([[1,0]]) == 0

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")