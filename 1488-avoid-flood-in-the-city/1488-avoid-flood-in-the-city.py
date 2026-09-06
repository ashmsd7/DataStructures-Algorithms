from bisect import bisect_right

##Revise solution again please
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        n = len(rains)
        hasher = {}
        drying = []

        for i in range(n):
            if rains[i] == 0:
                drying.append(i)
                continue
            
            lake = rains[i]

            if lake in hasher:
                rain = hasher[lake]
                index = bisect_right(drying,rain)

                if index == len(drying):
                    return []
                
                dry_day = drying[index]
                ans[dry_day] = lake
                drying.pop(index)
            
            hasher[lake] = i 

        for day in drying:
            ans[day] = 1
        return ans




        