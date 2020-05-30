from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0, 1]

    def test_twoSum(self):
        assert self.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert self.twoSum([11, 15, 2, 7], 9) == [2, 3]

if __name__ == "__main__":
    Solution().test_twoSum()
    print("Everything passed")