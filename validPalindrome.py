class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        lens = len(s)
        j = lens - 1
        for i in range(lens):
            while not s[j].isalnum() and j >= 0:
                j -= 1
            if not s[i].isalnum():
                continue
            if j < 0 or s[i].lower() != s[j].lower():
                return False
            j -= 1
        while not s[j].isalnum() and j >= 0:
            j -= 1
        return (True if j == -1 else False)
        
    def test(self):
        assert self.isPalindrome(" ") == True
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")