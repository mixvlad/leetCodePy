from typing import List
import sys

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lenn = len(nums)
        if lenn < 2:
            return nums
        p1 = p2 = sys.maxsize
        for i in range(lenn):
            if nums[i] == 0:
                if not p2 > i:
                    nums[p2], nums[i] = nums[i], nums[p2]
                    p2 = p2+1
                    if not p1 > i:
                        nums[p1], nums[p2 - 1] = nums[p2 - 1], nums[p1]
                        p1 = p1+1
                else:
                    if not p1 > i:
                        nums[p1], nums[i] = nums[i], nums[p1]
                        p1 = p1+1
            
            if nums[i] == 1:
                if not p2 > i:
                    if p1 > i:
                        p1 = p2
                    nums[p2], nums[i] = nums[i], nums[p2]
                    p2 = p2+1
                else:
                    if p1 > i:
                        p1 = i
            
            if nums[i] == 2:
                if p2 > i:
                    p2 = i
            
            
        return nums
    def test(self):
        assert self.sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")                