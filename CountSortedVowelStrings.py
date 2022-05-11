class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.comb(n, 5)

    def comb(self, n: int, avSymbNumb: int) -> int:
        res = 0
        
        if n > 0:
            for i in range(avSymbNumb):
                res += self.comb(n-1, avSymbNumb-i)
        elif n == 0:
            res += 1
            
        return res
        
    def test(self):
        assert self.countVowelStrings(1) == 5
        assert self.countVowelStrings(2) == 15
        assert self.countVowelStrings(33) == 66045

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")
