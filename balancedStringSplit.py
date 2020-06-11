from collections import deque
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lens = len(s)
        if lens < 2:
            return 0
        h = {"L": "R", "R":"L"}
        count = 0
        i = 1
        q = deque(s[0])
        for x in s[1:]:
            if q and q[-1] == h[x]:
                q.pop()
            else:
                q.append(x)
            if not q:
                count += 1
        return count
        
    def test(self):
        assert self.balancedStringSplit("RLRRLLRLRL") == 4

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")