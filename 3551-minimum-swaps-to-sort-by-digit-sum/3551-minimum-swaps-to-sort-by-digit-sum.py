class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #so basically im planning on calculating sum of digits of each number in the array and then store the values of its index in array, sum of digits and the element itself in a tuple

        tup = []

        for i in range(len(nums)):
            curr_tup = ()
            curr_str = str(nums[i])
            curr_sum = 0
            for ch in curr_str:
                curr_sum+=int(ch)
            
            curr_tup = (curr_sum, nums[i] , i)
            tup.append(curr_tup)
        
        #tuple array of all 
        tup.sort()

        #now we get sorted array according to indices, but then we need to find number of swaps

        #[18,16,34,43] -> [18,43,34,16] => [0,1,2,3] -> [0,3,2,1] , cycle detection

        n = len(nums)
        visited = [False] * n
        res = 0

        for i in range(n):
            if visited[i] or i==tup[i][2]:
                continue
            
            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True

                j = tup[j][2]
                cycle_size+=1
            
            if cycle_size>1:
                res+= cycle_size - 1
            
        return res









        