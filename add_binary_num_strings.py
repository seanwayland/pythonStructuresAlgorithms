class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        '''
        BINARY ALGORITHM ADDING FROM RIGHT TO LEFT 

        If the sum is 0, write a 0 in the answer’s fours place. 
        If the sum is 1, write a 1 in the answer’s fours place.
        If the sum is 2, write a 0 in the answer’s fours place, and carry a 1
        If the sum is 3, write a 1 on the answer’s fours place, and carry a 1  
        
        '''

        n = max(len(a), len(b))
        ### add leading zeroes if needed 
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        result = ""
        for i in range(1,n+1):
            j = -i
            aa = int(a[j])
            bb = int(b[j])
            row_sum = aa + bb + carry
            if(row_sum == 0):
                result = result + "0"
                carry = 0
            if(row_sum == 1):
                result = result + "1"
                carry = 0
            if(row_sum == 2):
                result  = result + "0"
                carry = 1
            if(row_sum == 3):
                result = result + "1"
                carry = 1
        # if a carry is left at end 
        if(carry == 1 ):
            result = result + "1"
        print(result)
        # reverse the result 
        return(result[::-1])
                
