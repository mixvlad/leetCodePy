from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_cost = sorted(costs,key = lambda x:x[0]-x[1])
        result = 0 
        for i in range(len(costs)):
            if i < len(costs) / 2:
                result += sorted_cost[i][0]
            else:
                result += sorted_cost[i][1]
        return result

    def test(self):
        # assert self.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110
        assert self.twoCitySchedCost([[10,1000],[1,1000],[2,1000],[20000,100000],[2000000,100000],[20000,100000]]) == 2003

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")