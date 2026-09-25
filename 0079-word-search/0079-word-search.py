class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        #Doing DFS at every cell that matches with word[0]


        def dfs(r,c,visited,index):
            if r<0 or r==rows or c<0 or c==cols:
                return False
            
            if (r,c) in visited:
                return False
            
            if board[r][c]!= word[index]:
                return False
            
            if index == len(word) - 1:
                return True #If we reach index that is equal to length of word we will go out so return True
            
            visited.add((r,c))
            directions = [(-1,0),(1,0),(0,1),(0,-1)]

            for nr , nc in directions:
                nr = r + nr
                nc = c + nc

                if dfs(nr,nc,visited,index+1):
                    return True #Checking if next one is valid also
                
            visited.remove((r,c)) #Invalid vertex so return False there directly, using new visited set for every vertex we traverse in bottom for loops.

            return False



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    if dfs(r,c,visited,0):
                        return True
        
        return False
        