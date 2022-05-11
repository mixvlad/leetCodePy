from functools import lru_cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        @lru_cache
        def recursive(n: int, avSymbNumb: int):
            if n < 1:
                return 1

            res = 0
            
            for i in range(avSymbNumb):
                res += recursive(n-1, avSymbNumb-i)
                
            return res
            
        return recursive(n, 5)
        
    def test(self):
        assert self.countVowelStrings(1) == 5
        assert self.countVowelStrings(2) == 15
        assert self.countVowelStrings(33) == 66045

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")
