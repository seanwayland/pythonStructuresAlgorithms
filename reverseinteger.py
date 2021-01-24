class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = str(x)
        neg = 0
        print(res)
        if res[0] == '-':
            neg = 1
            res = res[1:]
        res = res[::-1]
        res = res.lstrip("0")
        if (abs(int(res)) > 2**31):
            return 0
        if neg == 1 :
            return '-' + res
        else:
            return res
            
