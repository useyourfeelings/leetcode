class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    tester = [0 for i in range(0, 10)]
    
    def init_tester(self):
        for i in range(1, 10):
            self.tester[i] = 0
        
    def isValidSudoku(self, board):
        for i in range(0, 9):
            self.init_tester()
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if self.tester[num] == 1:
                    return False
                self.tester[num] = 1
        
        for i in range(0, 9):
            self.init_tester()
            for j in range(0, 9):
                if board[j][i] == '.':
                    continue
                num = int(board[j][i])
                if self.tester[num] == 1:
                    return False
                self.tester[num] = 1
                
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                self.init_tester()
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] == '.':
                            continue
                        num = int(board[x][y])
                        if self.tester[num] == 1:
                            return False
                        self.tester[num] = 1
                        
        return True
