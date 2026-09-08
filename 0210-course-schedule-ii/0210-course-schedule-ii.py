class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []
        graph = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        for relation in prerequisites:
            graph[relation[1]].append(relation[0])
            indegree[relation[0]]+=1
        

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        visited = 0
        while q:
            course = q.popleft()
            res.append(course)
            visited+=1
            for relation in graph[course]:
                indegree[relation]-=1
                if indegree[relation] == 0:
                    q.append(relation)
        
        return res if visited == numCourses else []
        