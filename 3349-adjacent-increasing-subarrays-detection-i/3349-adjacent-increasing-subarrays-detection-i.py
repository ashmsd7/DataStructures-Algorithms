class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        #Optimal approach -> Keep track of two windows, prev and curr where prev discusses the preceding increasing run and curr discusses the current increasing run. 

        #Say, we have nums = [2,5,7,8,9,2,3,4,3,1] with k = 3.. we see [7,8,9] & [2,3,4] are two different runs but still satisfy the condition so that is why we keep track of prev and curr. 

        #In another example , say nums = [1,2,3,4,5,6,7] with k =2, the entire nums array comes under only ONE run, so at each curr iteration we check if value of curr >= 2*k if yes then it can be divided into 2 different runs

        #Say we have nums = [1,2,3,2,1,2,3] with k = 3, now we have two different runs [1,2,3] & [1,2,3] that are increasing but are not adjacent, so for this we need to update prev and curr after EVERY run.
        if k == 1:
            return len(nums)>=2
        n = len(nums)
        curr = 1
        prev = 0

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                curr+=1
            if curr>=2*k:
                return True
            
            if min(prev,curr) >=k:
                return True

            if nums[i] >=nums[i+1]:
                prev = curr
                curr = 1
        return False



        