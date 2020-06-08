from typing import List
import random

class Solution:
    w = []
    def __init__(self, w: List[int]):
        random.seed()
        self.w = w

    def pickIndex(self) -> int:
        return random.choices(range(len(self.w)), self.w)[0]
    
    def test(self):
        assert self.pickIndex() < 1

if __name__ == "__main__":
    Solution([1]).test()
    print("Everything passed")