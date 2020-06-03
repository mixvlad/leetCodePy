class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) <= len(haystack):
            i = 0
            while i <= len(haystack) - len(needle):
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    if j + 1 == len(needle):
                        return i
                i += 1
                
        
        return -1
    
    def test(self):
        assert self.strStr("a", "a") == 0
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")