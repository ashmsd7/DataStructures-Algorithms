class TimeMap:

    def __init__(self):
        self.hasher = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hasher:
            self.hasher[key] = []
        self.hasher[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hasher:
            return ""
        arr = self.hasher[key]
        result = ""

        l = 0
        r = len(arr)-1
        result = ""

        while l<=r:
            mid = (l+r)//2
            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
        return result



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)