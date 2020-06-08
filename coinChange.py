from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = [0 for k in range(amount+1)] 
  
        # Base case (If given value is 0) 
        table[0] = 1
    
        # Pick all coins one by one and update the table[] values 
        # after the index greater than or equal to the value of the 
        # picked coin 
        for i in range(0,len(coins)): 
            for j in range(coins[i],amount+1): 
                table[j] += table[j-coins[i]] 
    
        return table[amount] 
    
    def test(self):
        # assert self.change(5, [1,2,5]) == 4, self.change(5, [1,2,5])
        # assert self.change(3, [2]) == 0
        # assert self.change(10, [10]) == 1
        # assert self.change(5, [10]) == 0
        # assert self.change(5, [1,2,3,5]) == 6, self.change(5, [1,2,3,5])
        val = self.change(200, [3,5,7,8,9,10,11])
        assert val == 6, val
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")