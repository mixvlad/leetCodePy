class Solution:
    def isHappy(self, n: int) -> bool:
        cur = n
        seen = []
        while not cur in seen:
            seen.append(cur)
            digits = [int(x) for x in str(cur)]
            newDig = 0
            for i in digits:
                newDig += i*i
            
            if newDig == 1:
                return True
            cur = newDig
        return False
        
    def test(self):
        assert self.isHappy(19) == True
        assert self.isHappy(2) == False
          

    
if __name__ == "__main__":
  Solution().test()
  print("Everything passed")