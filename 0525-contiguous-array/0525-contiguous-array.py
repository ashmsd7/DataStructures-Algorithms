class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = []
        count = 0
        hasher = {0:-1}
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count-=1
            else:
                count+=1
            prefix.append(count)
            if count not in hasher:
                hasher[count] = i
            else:
                max_len = max(max_len, i-hasher[count])
        
        return max_len
        

        