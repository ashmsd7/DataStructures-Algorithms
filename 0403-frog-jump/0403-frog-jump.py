class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n = len(stones)
        if stones[1]!=1:
            return False
        
        dp = [[False]* (n+1) for _ in range(n)]
        dp[0][0] = True
        dp[1][1] = True

        #dp[stone][k] = stored values.
        stone_index = {stone:i for i,stone in enumerate(stones)}

        for i in range(1,n):
            for k in range(1,n+1):
                if not dp[i][k]:
                    continue
                
                for next_k in (k-1,k,k+1):
                    if next_k <=0 :
                        continue
                    
                    next_stone = stones[i] + next_k

                    if next_stone in stone_index:
                        idx = stone_index[next_stone]
                        dp[idx][next_k] = True
                
        for k in range(n):
            if dp[n-1][k]:
                return True
        
        return False
        








        