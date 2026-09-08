class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        start = newInterval[0]
        end = newInterval[1]
        

        for i in range(len(intervals)):
            # // To the left
            if intervals[i][1] < start :
                res.append(intervals[i])
            # // To the right
            elif intervals[i][0] > end:
                res.append([start,end])
                res.extend(intervals[i:])
                return res
                
            # // If any merging, deal with both ends
            else:

                start = min(start,intervals[i][0])
                end = max(end,intervals[i][1])
        res.append([start,end])

        return res
        