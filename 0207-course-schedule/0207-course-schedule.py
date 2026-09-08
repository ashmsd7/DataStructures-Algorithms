class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree_list = [0] * numCourses

        for relation in prerequisites:
            indegree_list[relation[0]]+=1
            graph[relation[1]].append(relation[0])
            
        q = deque()

        for i in range(len(indegree_list)):
            if indegree_list[i] == 0:
                q.append(i)
        
        visited = 0
        while q:
            course = q.popleft()
            visited+=1
            for relation in graph[course]:
                indegree_list[relation]-=1
                if indegree_list[relation] == 0:
                    q.append(relation)
            
        return visited == numCourses

    

        

        