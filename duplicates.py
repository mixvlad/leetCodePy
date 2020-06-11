from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
     
        count = {nums[0]: 0}
        print(count)
        for i in range(1, len(nums)):
            if nums[i] in count and i - count[nums[i]] <= k:
                return True
            count[nums[i]] = i # updates the rightmost index of each value in the array
            
            print(count)
        return False

    def test(self):
        assert self.containsNearbyDuplicate([1,2,3,1,2,3], k = 2) == False

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")
