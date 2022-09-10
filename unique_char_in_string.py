class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for i in range(len(s)):
            if count[(s[i])] == 1:
                return i
        return -1
