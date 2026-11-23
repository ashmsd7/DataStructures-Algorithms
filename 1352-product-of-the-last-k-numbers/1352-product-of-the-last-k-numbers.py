class ProductOfNumbers:
    def __init__(self):
        self.lister = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.lister = [1]
        else:
            self.lister.append(num * self.lister[-1])

    def getProduct(self, k: int) -> int:
        n = len(self.lister)

        if k>=len(self.lister):
            return 0
        else:
            return self.lister[-1] // self.lister[-k-1]
        
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)