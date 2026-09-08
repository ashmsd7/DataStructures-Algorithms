class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        h1 = {i:0 for i in range(1,n+1)}
        h2 = {i:0 for i in range(1,n+1)}

        for relation in trust:
            h1[relation[0]] = h1.get(relation[0],0)+1
            h2[relation[1]] = h2.get(relation[1],0) + 1

        for key,val in h1.items():
            if val == 0:
                if h2[key] == n-1:
                    return key
        return -1
        