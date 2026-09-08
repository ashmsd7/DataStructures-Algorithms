class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key = lambda x:x[1])   

        current_day = 0
        selected = []

        for duration,deadline in courses:
            selected.append(duration)
            current_day+=duration

            if deadline < current_day:
                longest_course = max(selected)
                selected.remove(longest_course)
                current_day-=longest_course
        
        return len(selected)

        