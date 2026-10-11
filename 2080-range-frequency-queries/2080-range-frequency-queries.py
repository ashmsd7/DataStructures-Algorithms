class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.hasher = {}
        for i,val in enumerate(arr):
            if val not in self.hasher:
                self.hasher[val] = []
            
            self.hasher[val].append(i) 
        
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.hasher:
            return 0
        
        indices = self.hasher[value]
        
        #now lets use bisect_left and bisect_right

        start = bisect_left(indices,left)
        end = bisect_right(indices,right) 

        #Here, we are basically checking where we can insert left and right in the indices array such that indices is still sorted.

        return end - start
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)