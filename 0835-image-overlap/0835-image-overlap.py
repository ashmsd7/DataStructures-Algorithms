class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        #Optimized => Store all indices r1,c1 and r2,c2 where img1[r1][c1] == 1 and img2[r2][c2] == 1. Then, use a hashmap to store the number of transitions which would be (r2-r1,c2-c1). For each pair of points in both lists, calculate the transition value and store that index into hashmap. return the transition value in hashmap that occured the most times.


        img1_ones = []
        img2_ones = []

        d = defaultdict(int)

        n = len(img1)

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    img1_ones.append((r,c))


        for r in range(n):
            for c in range(n):
                if img2[r][c] == 1:
                    img2_ones.append((r,c))
            
        
        for r1 , c1 in img1_ones:
            for r2 , c2 in img2_ones:
                d[(r2-r1,c2-c1)]+=1
        
        return max(d.values() or [0])
        



        