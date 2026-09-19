class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        #As confusing as it looks, we are just checking if adding the previous sum to the current variable will hurt the total value. 

        #Meaning -> If current variable is better off without the prev array sum, it means we would want to start the array for our current variable rather than the index usedto calculate the previous sum. Then, we compare it with the global best sum we are using.


        best_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1,len(nums)):
            curr_sum = max(nums[i], nums[i] + curr_sum)
            best_sum = max(best_sum,curr_sum)
        
        return best_sum
            


        