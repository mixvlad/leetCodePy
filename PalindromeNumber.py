from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed = 0
        while x > reversed:
            x, newRev = divmod(x, 10)
            reversed = reversed * 10 + newRev
            
        return x == reversed or x == reversed // 10

    def test(self):
        assert self.isPalindrome(121) == True
        assert self.isPalindrome(123) == False
        assert self.isPalindrome(0) == True
        assert self.isPalindrome(5) == True
        assert self.isPalindrome(-5) == False

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")