from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: 1 if len(str(x)) % 2 == 0 else 0, nums))

    def test(self):
        assert self.findNumbers([555,901,482,1771]) == 1 

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")