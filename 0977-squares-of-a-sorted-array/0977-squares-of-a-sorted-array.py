class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        write = len(nums)-1
        arr = [0]*len(nums)

        while l<=r:
            if pow(nums[l],2)<pow(nums[r],2):
                arr[write] = pow(nums[r],2)
                r-=1
            else:
                arr[write] = pow(nums[l],2)
                l+=1
            write-=1
        return arr


