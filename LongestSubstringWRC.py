from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        queue = deque(maxlen = len(s))
        added_nums = set([])
        for x in s:
            if x in added_nums:
                cur_q_len = len(queue)
                if max < cur_q_len:
                    max = cur_q_len
                while True:
                    p = queue.popleft()
                    added_nums.remove(p)
                    if p == x:
                        break
            
            added_nums.add(x)
            queue.append(x)
                
        cur_q_len = len(queue)
        if max < cur_q_len:
            max = cur_q_len
        return max
        
    def test(self):
        assert self.lengthOfLongestSubstring("aac") == 2

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")