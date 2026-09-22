class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        #You are using a current end variable which as we keep traversing will discuss through overlapping intervals and merge them.


        meetings.sort()
        current_end = 0
        res = 0

        for i in range(len(meetings)):
            start = meetings[i][0]
            end = meetings[i][1]

            if start > current_end:
                #Basically, if two schedules dont overlap, we find the in between, say [1,3] & [5,6] -> bw is 5 - 3 - 1 = 1 day which is 4th day. (start = 5, current_end = 3)
                
                res+= start - current_end -1
            
            current_end = max(current_end , end) #Extending current_end to the next interval.
        
        res+= days - current_end #Finally , outside the maximum interval. 

        return res

            

        