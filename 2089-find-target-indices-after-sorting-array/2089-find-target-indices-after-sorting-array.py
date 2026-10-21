class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt = 0
        targ = 0
        for num in nums:
            if num < target:
                cnt+=1
            elif num == target:
                targ+=1
        
        res = []
        it = 0
        while targ:
            res.append(cnt + it)
            it+=1
            targ-=1

        return res
            
        