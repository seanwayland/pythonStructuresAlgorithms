class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.matrix = board
        self.finished = False
        self.backtrack()

    def backtrack(self, row=0, col=0):
        if row == 9 and col == 0:
            self.finished = True
            return
        if self.matrix[row][col] != '.':
            self.backtrack(*list(self.index_update(row, col)))
            return
        for num in [str(i) for i in range(1, 10)]:
            if self.is_valid(num, row, col):
                self.matrix[row][col] = num
                self.backtrack(*list(self.index_update(row, col)))
                if self.finished:
                    return
                self.matrix[row][col] = '.'
        return

    def ind(self, row):
        index = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        if row <= 2:
            r_i = index[0]
        elif row <= 5:
            r_i = index[1]
        else:
            r_i = index[2]
        return r_i

    def is_valid(self, val, row, col):
        if val in self.matrix[row][:] or val in [self.matrix[i][col] for i in range(9)]:
            return False
        r_i = self.ind(row)
        c_i = self.ind(col)
        if val in [self.matrix[r][c] for r in r_i for c in c_i]:
            return False
        return True

    def index_update(self, row, col):
        if col + 1 > 8:
            row += 1
        col = (col + 1) % 9
        return row, col