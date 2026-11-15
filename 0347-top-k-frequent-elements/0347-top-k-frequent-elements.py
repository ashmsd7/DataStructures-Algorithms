class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        cnt = Counter(nums)

        sort_cnt = sorted(cnt.items(), key= lambda x:x[1], reverse=True)

        res = [key for key,value in sort_cnt[:k]]
        return res

        