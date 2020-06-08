class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False    
            
        return ( n & ( n-1 ) ) == 0
    
    def test(self):
        assert self.isPowerOfTwo(2) == True
        assert self.isPowerOfTwo(23) == False
        assert self.isPowerOfTwo(22222222222222) == False
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")