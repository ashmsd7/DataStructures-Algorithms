class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0 

        for left in range(len(nums)):
            product = 1
            gcd = 0
            lcm = 1
            for right in range(left,len(nums)):
                val = nums[right]
                product*=val
            
                gcd = math.gcd(gcd,val)
                lcm = math.lcm(lcm,val)

                if product == gcd*lcm:
                    res = max(res,right-left+1)
        
        return res