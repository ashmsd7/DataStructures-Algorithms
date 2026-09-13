class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        max_overlap = 0
        n = len(img1)

        for sr in range(-n+1,n):
            for sc in range(-n+1,n):
                overlap = 0
                for r in range(n):
                    for c in range(n):
                        nr , nc = r + sr , c + sc
                        if 0<=nr<n and 0<=nc<n:
                            if img1[r][c] == 1 and img2 [nr][nc] == 1:
                                overlap+=1

                max_overlap = max(overlap,max_overlap)

        return max_overlap 



        

        






        