class Solution:
    
    def merge_sort(self,left,right):
        res = []
        i = j = 0

        while i< len(left) and j<len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        result = self.merge_sort(nums1,nums2)
        k = len(result)
        if k % 2 == 0:
            return (result[k//2] + result[(k//2)-1] )/2
        else:
            return result[k//2]
         
        

