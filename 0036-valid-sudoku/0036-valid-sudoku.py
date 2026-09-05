class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        grid = [set() for _ in range(n)]
        
        for row in range(n):
            for col in range(n):
                if board[row][col] == '.':
                    continue
                
                box = (row // 3) * 3 + col // 3 

                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in grid[box]:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                grid[box].add(board[row][col])
            
        return True
                        
        