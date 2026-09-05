class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        grid = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num != '.':
                    rows[row].add(num)
                    cols[col].add(num)
                    box = (row // 3) * 3 + col // 3
                    grid[box].add(num)
        
        def backtrack():
            best_cell = None
            best_candidate = None
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == '.':
                        box = (row // 3) * 3 + col // 3
                        taken = rows[row] | cols[col] | grid[box]
                        curr_candidate = set('123456789') - taken

                        if not curr_candidate :
                            return False

                    
                        if best_candidate is None or len(curr_candidate) < len(best_candidate):
                            best_cell = (row,col)
                            best_candidate = curr_candidate

                        if len(best_candidate) == 1 :
                            break

                    if best_candidate is not None and len(best_candidate) == 1:
                        break
                
            if best_cell is None:
                return True
                
            row , col = best_cell
            box = row // 3 * 3 + col //3
            
            for num in best_candidate:
                board[row][col] = num
                rows[row].add(num)
                cols[col].add(num)
                grid[box].add(num)

                if backtrack():
                    return True
                
                board[row][col] = '.'
                rows[row].remove(num)
                cols[col].remove(num)
                grid[box].remove(num)
            return False
        
        backtrack()



                        
                    
                    


                    


        