from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        end = False
        index = 0
        if not strs:
            return ''

        while index < len(strs[0]):
            cur = strs[0][index]
            for x in strs[1:]:
                if len(x) <= index or x[index] != cur:
                    end = True
                    break
            if(end):
                break
            else:
                res += cur
                index += 1
        
        return res
    
    def test(self):
        assert self.longestCommonPrefix(["flower","flow","flight"]) == "fl"
        assert self.longestCommonPrefix(["dog","racecar","car"]) == ""
        assert self.longestCommonPrefix([]) == ""
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        