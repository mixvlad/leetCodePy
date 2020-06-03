class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }
        ret = 0
        for k, v in mappings.items():
            while s.startswith(k):
                ret += v
                s = s[len(k):]
        return ret
    
    def test(self):
        assert self.romanToInt("III") == 3
        assert self.romanToInt("IV") == 4
        assert self.romanToInt("IX") == 9
        assert self.romanToInt("LVIII") == 58
        assert self.romanToInt("MCMXCIV") == 1994
        assert self.romanToInt("MMMCDXC") == 3490

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        