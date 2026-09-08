class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])

        selected = []
        current_day = 0
        
        for duration , deadline in courses:
            current_day+= duration
            heapq.heappush(selected,-duration)

            if current_day > deadline:
                longest = -heapq.heappop(selected)
                current_day-=longest
            
        
        return len(selected)
        