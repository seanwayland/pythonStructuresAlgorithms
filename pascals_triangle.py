    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([])
        for i in range(numRows):
            current_row = [1]
            for j in range(i):
                print(i,j)
                if( j == i - 1 ):
                    current_row.append(1)
                else:
                    #  j is going from 0 to rowlength - 1 
                    # i is is going from 1 to numrows - 1 
                    sum_val = result[i][j] + result[i][j+1]
                    current_row.append(sum_val)
                
                   # current_row.append(2)
                print(current_row)
            result.append(current_row)
            
        result.pop(0)
        return result
