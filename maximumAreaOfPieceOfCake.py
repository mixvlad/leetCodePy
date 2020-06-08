from typing import List

class Solution:
    def getMax(self, max: int, cuts: List[int]) -> int:
        last = 0
        for x in cuts:
            cur = x - last
            if cur > max:
                max = cur
            last = x
        return max
    
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 1000000007
        horizontalCuts.sort()
        verticalCuts.sort()
        maxh = self.getMax(h - horizontalCuts[-1], horizontalCuts)
        maxv = self.getMax(w - verticalCuts[-1], verticalCuts)
        
        return maxh%mod * maxv%mod

    def test(self):
        assert self.maxArea(50, 15, [37,40,41,30,27,10,31],[2,1,9,5,4,12,6,13,11]) == 51
        
if __name__ == "__main__":
    Solution().test()
    print("Everything passed")