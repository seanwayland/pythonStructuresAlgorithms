class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def get_num_from_char(ch):
            return (ord(ch) - 64)
        l = len(columnTitle)
        result = 0
        
        for i in range(l):
            print(l-i)
            result = result + get_num_from_char(columnTitle[i])*(26**(l-i-1))
        return result
