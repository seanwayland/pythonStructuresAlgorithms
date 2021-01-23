class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCP = ""
        if strs is None or len(strs) == 0:
            return LCP
        index = 0
        for c in strs[0]:
            for i in range (1, len(strs)):
                if index > len(strs[i])-1 or c!= strs[i][index]:
                    return LCP
                
            LCP = LCP + c
            index = index + 1
        return LCP
