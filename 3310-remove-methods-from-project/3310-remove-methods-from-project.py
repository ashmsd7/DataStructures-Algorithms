class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        grapher = [[] for _ in range (n)]
        suspicious = set()
        result = []

        for u , v in invocations:
            grapher[u].append(v)
        
        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for connection in grapher[node]:
                dfs(connection)
        dfs(k)
        for u , v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        for i in range(n):
            if i not in suspicious:
                result.append(i) 
        
        return result 