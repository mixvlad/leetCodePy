class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
       
    def test(self):
        assert self.canWinNim(4) == False
        assert self.canWinNim(1) == True
        assert self.canWinNim(2) == True

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")
