class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        lenn = len(name)
        lent = len(typed)
        if lent < lenn:
            return False
        i, j = 1, 0
        while i < lent:
            if j < lenn and typed[i] == name[j]:
                i += 1
                j += 1
            elif j > 0 and typed[i] == name[j - 1]:
                i += 1
            else:
                return False
            
        return True
    def test(self):
        assert self.isLongPressedName("laiden", "laiden") == True
        assert self.isLongPressedName("a", "s") == False

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")                        