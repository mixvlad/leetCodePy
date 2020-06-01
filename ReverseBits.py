class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def test(self):
        assert self.reverseBits(43261596) == 964176192, self.reverseBits(43261596)
        assert self.reverseBits(4294967293) == 3221225471
        
if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        