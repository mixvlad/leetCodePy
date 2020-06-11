from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 1
        solutions = {1: 1, 2: 2}
        for i in range(3, n + 1):
            solutions[i] = solutions[i - 1] + solutions[i - 2]
        
        return solutions[n]

    def test(self):
        assert self.climbStairs(0) == 1
        assert self.climbStairs(1) == 1
        assert self.climbStairs(2) == 2
        assert self.climbStairs(3) == 3
        assert self.climbStairs(4) == 5
        assert self.climbStairs(5) == 8
        assert self.climbStairs(6) == 13
        assert self.climbStairs(7) == 21

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")