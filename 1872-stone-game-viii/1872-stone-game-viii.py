class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        k = len(stones)
        prefix_sum = [0] * k
        prefix_sum[0] = stones[0]
        for i in range(1,k):
            prefix_sum[i] = prefix_sum[i-1] + stones[i]

        res = prefix_sum[-1]

        for i in range(k-2,0,-1):
            res = max(res,prefix_sum[i]-res)

        return res
        
        


        
