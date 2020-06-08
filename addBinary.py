class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        add = 0
        i = 0
        a = a[::-1]
        b = b[::-1]
        while True:
            val1  = (int(a[i]) if i < len(a) else 0)
            val2  = (int(b[i]) if i < len(b) else 0)
            
            add, cur = divmod(val1 + val2 + add, 2)    
            i += 1
            res = str(cur) + res

            if i >= len(a) and i >= len(b) and not add:
                break
            
        return res

    def test(self):
        assert self.addBinary("1010", "1011") == "10101"
        assert self.addBinary("0", "0") == "0"
        
if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        