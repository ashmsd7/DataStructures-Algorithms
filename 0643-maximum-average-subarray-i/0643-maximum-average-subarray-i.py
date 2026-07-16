class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        i = 0
        j = i + k

        while j<=(len(nums)-1):
            curr_sum+=nums[j]-nums[i]
            max_sum = max(max_sum,curr_sum)
            i+=1
            j+=1
        return max_sum / k



        