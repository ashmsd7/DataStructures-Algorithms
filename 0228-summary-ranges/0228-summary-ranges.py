class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        lower = nums[0]
        higher = nums[0]
        res = []

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i]!=1:
                if lower == higher:
                    res.append(str(lower))
                else:
                    res.append(f"{lower}->{higher}")
                lower = nums[i+1]
                higher = nums[i+1]
            else:
                higher = nums[i+1]
        
        if lower == higher:
            res.append(str(lower))
        else:
            res.append(f"{lower}->{higher}")
        return res 