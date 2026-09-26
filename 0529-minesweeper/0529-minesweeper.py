class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # Wow. Did i just code a MineSweeper game? Anyways, so firstly , we call dfs on the click cell. Basically, we are expected to calculate the state of the board once the click happens.


        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):

            #If click cell is Mine, then just return the board with M -> X
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return
            
            elif board[r][c]!='E':
                return #If it is either B or a digit, it means we need not process it as its already been processed.
            
            directions = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
            num_mines = 0

            #This is the meat of the problem. Here we break the problem into two steps. 1) Figure out how the cells modify. 2) Decide which neighboring cells to call DFS on.

            for nr , nc in directions:
                nr = r + nr
                nc = c + nc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if board[nr][nc] == 'M':
                        num_mines+=1

                        #Here, we keep track of all the mines that neighbor our current (r,c). If it does not have any neighboring mines, it automatically means its an explored empty cell ('B'). Else, we modify it with a digit that would be str(num_mines).

            if num_mines == 0:
                board[r][c] ='B'

                for nr , nc in directions:
                    nr = r + nr
                    nc = c + nc
                #In this loop, we deal with the neighboring cells that are still 'E' because we need to process all the E cells to get the final board state. We call DFS on all the E cells.
                    if nr >=0 and nr < rows and nc >=0 and nc<cols:
                        if board[nr][nc] == 'E':
                            dfs(nr,nc)
            else:
                board[r][c] = str(num_mines)
        
        
        clickR = click[0]
        clickC = click[1]

        dfs(clickR,clickC)
        return board #In-place
            
            
            
                


            

            

                    
        

        