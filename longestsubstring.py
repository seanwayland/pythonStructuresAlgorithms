class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp: 
                // if the value is in the hashmap move the sliding start to its highest pos 
                i = max(mp[s[j]], i)
            // if this is the longest substring store its value    
            ans = max(ans, j - i + 1)
            // add the character to the map using one greater than index. this will change if it exists 
            mp[s[j]] = j + 1

        return ans
        
