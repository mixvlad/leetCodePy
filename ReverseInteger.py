class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:  # handle positive numbers  
            a =  int(str(x)[::-1])  
        if x <=0:  # handle negative numbers  
            a = -1 * int(str(x*-1)[::-1])  
        # handle 32 bit overflow  
        mina = -2**31  
        maxa = 2**31 - 1  
        if a not in range(mina, maxa):  
            return 0  
        else:  
            return a

    def test(self):
        assert self.reverse(123) == 321
        assert self.reverse(-123) == -321
        assert self.reverse(120) == 21
        assert self.reverse(1563847412) == 0
        assert self.reverse(7463847412) == 2147483647
        

        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        