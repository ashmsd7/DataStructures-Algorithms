class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        #Brute force -> Generate all k length subarrays that are adjacent and compare them

        
        n = len(nums)


        for i in range(n - 2*k + 1):
            first = nums[i:i+k]
            second = nums[i+k:i+2*k]
            valid = True
            for l in range(k-1):
                if first[l] >= first[l+1] or second[l] >= second[l+1]:
                    valid = False
            
            if valid:
                return True
            
        return False




        





        