from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxcurr = nums[0]
        maxglobal = nums[0]
        for i in range(1,len(nums)):
            maxcurr = max(nums[i], maxcurr + nums[i]) 
            maxglobal = max(maxcurr, maxglobal)
        return maxglobal

    def test(self):
        # assert self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
        # assert self.maxSubArray([-1]) == -1
        # assert self.maxSubArray([1]) == 1
        # assert self.maxSubArray([-2,-3,-1]) == -1
        assert self.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]) == 6
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")