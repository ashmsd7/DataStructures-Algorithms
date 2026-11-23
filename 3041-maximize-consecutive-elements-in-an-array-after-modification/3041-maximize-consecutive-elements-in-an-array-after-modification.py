class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        #[1,1,1,2,5] -> after sorted.

        #next enti ?
        nums.sort()
        n = len(nums)
        dp = {}
        result = 0

        for x in nums:
            #longest sequence ending at current value 
            dp[x+1] = max(dp.get(x+1,0),dp.get(x,0)+1)

            #for last case 
            dp[x] = max(dp.get(x,0),dp.get(x-1,0)+1)

            result = max(result,dp[x],dp[x+1])

        return result


        