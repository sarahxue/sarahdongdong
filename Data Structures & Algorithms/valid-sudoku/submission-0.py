class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force, check row, col, box 
        # time: O(n^2), space: O(n)
        # check rows 
        for i in range(9):
            seen = set()
            for j in range (9):
                if (board[i][j] != "."):
                    if (board[i][j]) in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        # check cols
        for j in range(9):
            seen = set()
            for i in range (9):
                if (board[i][j] != "."):
                    if (board[i][j]) in seen:
                        return False
                    else:
                        seen.add(board[i][j])

        #check 3x3 box
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    # box row
                    row = (square//3) * 3 + i
                    # box col 
                    col = (square % 3) * 3 + j
                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        return True
