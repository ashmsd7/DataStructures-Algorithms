class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1]*n
        for i in range(1,n):
            product[i] = product[i-1] * nums[i-1]
        
        K = 1
        for i in range(n-1 , -1 , -1):
            product[i] = product[i] * K
            K = K * nums[i]
        
        return product


        
        