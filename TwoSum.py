from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for num_index, num in enumerate(nums):
            n = target-num
            if (n) in num_set:
                return [num_set[n], num_index]
            num_set[num] = num_index

    def test_twoSum(self):
        assert self.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert self.twoSum([11, 15, 2, 7], 9) == [2, 3]
        assert self.twoSum([11, 4, 2, 6], 8) == [2, 3]

if __name__ == "__main__":
    Solution().test_twoSum()
    print("Everything passed")