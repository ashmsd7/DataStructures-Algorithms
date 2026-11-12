class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # planning a two pass solution, one to check for all increasing subarrays and one to check all decreasing subarrays

        #but we can trak both increasing and decreasing subarrays in one pass only

        maxLen = 1
        inc = 1
        dec = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc+=1
                dec = 1
            elif nums[i] > nums[i+1]:
                inc = 1
                dec+=1
            # two equal elements(neither increasing nor decreasing)
            else:
                inc = 1
                dec = 1
            maxLen = max(inc,dec,maxLen)
    
        return maxLen



        