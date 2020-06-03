from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if(len_ != i):
                    nums[len_] = nums[i]
                len_ +=1
        return len_
    
    def test(self):
        # assert self.removeDuplicates([1,1,2]) == 2
        assert self.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5, self.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")