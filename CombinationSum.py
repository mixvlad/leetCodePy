from audioop import reverse
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        avNums = []
        for i in range(1, 10):
            avNums.append(i)
        res = self.comb(k, n, avNums)
        for x in res:
            x.sort()
        return res

    def comb(self, k: int, n: int, availableNums: List[int]) -> List[List[int]]:
        res = []
        
        if k > 1 and n > 0:
            for num in availableNums:
                innerChains = self.comb(k-1, n-num, [x for x in availableNums if x != num])
                if len(innerChains) > 0:
                    for y in innerChains:
                        y.append(num)
                    res.extend(innerChains)
                availableNums = availableNums[1:]
        elif k == 1 and n in availableNums:
            res.append([n])
            
        return res
        
    def test(self):
        assert self.combinationSum3(4,1) == []
        assert self.combinationSum3(3,7) == [[1,2,4]]
        assert self.combinationSum3(3,9) == [[1,2,6],[1,3,5],[2,3,4]]

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")
