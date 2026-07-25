class Solution:
    def maxProduct(self, n: int) -> int:
        nums = [int(d) for d in str(n)]
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    res = max(res,nums[i]*nums[j])
        return res