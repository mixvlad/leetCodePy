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
        
     