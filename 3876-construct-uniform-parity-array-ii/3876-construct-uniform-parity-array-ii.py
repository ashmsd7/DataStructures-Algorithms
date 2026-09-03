class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_num = float('inf')
        for num in nums1:
            if (num%2)!=0:
                odd_num = min(num,odd_num)
        
        if odd_num == float('inf'):
            return True 
        
        for i in range(len(nums1)):
            if nums1[i]%2 == 0 and (nums1[i] - odd_num < 1):
                return False
        return True 
        
        