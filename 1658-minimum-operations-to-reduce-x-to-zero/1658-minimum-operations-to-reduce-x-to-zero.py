class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        Arr_sum = 0
        for num in nums:
            Arr_sum+= num
        
        max_len = 0
        left = 0
        curr_sum = 0
        Target = Arr_sum - x

        if Target<0:
            return -1

        if Target == 0:
            return len(nums)

        for right in range(len(nums)):
            curr_sum+= nums[right]
            while curr_sum > Target:
                curr_sum-=nums[left]
                left+=1
            
            if curr_sum == Target:
                max_len = max(max_len,right-left+1)
    
        if max_len == 0:
            return -1

        return len(nums) - max_len


            





        