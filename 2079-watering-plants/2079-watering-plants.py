class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        curr = capacity
        total_steps = 0

        for i in range(len(plants)):
            if plants[i] <= curr:
                curr-=plants[i]
                total_steps+=1
            elif plants[i] > curr:
                total_steps+=2*i+1
                curr = capacity - plants[i]
        
        return total_steps



            
        