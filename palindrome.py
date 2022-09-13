class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(ch for ch in s if ch.isalnum())
        s2 = s1.lower()
        s4 = s2
        s3 = s2[::-1]
        return s3 == s4
    ## alternate start in middle and traverse outwards with pointers 
