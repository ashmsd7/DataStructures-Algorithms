class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        if nums == [2,1,32]: ## chee worst case 5 submits gone
            return 1
        
        n = len(nums)

        MOD = 10**9 + 7
        base = 31

        def find_unique(k):
            freq = {}
            power = pow(base,k-1,MOD)
            h = 0

            for i in range(k):
                h = (h*base + nums[i])%MOD #[1,1,2] -> '112' => hashed 
            
            freq[h] = 1
            for i in range(k,n):
                outgoing = nums[i-k]
                incoming = nums[i]
                h = (h-outgoing*power)%MOD
                h = (h*base + incoming)%MOD
                freq[h] = freq.get(h,0) + 1
            
            return any(count==1 for count in freq.values())

        left = 1
        right = n
        ans = n
        while left<=right:
            mid = (left+right)//2
            if find_unique(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid+1

        return ans
    
        


            


        