# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head.next
        prev = head
        arr = []
        idx = 1

        while curr.next: 
            if prev.val < curr.val and curr.val > curr.next.val:
                arr.append(idx)
            if prev.val > curr.val and curr.val < curr.next.val:
                arr.append(idx)
            
            prev = prev.next
            curr = curr.next

            idx+=1

        if len(arr)<2:
            return [-1,-1]

        minimum = float('inf')
        maximum = arr[-1] - arr[0]

        for i in range (1,len(arr)):
            minimum = min(minimum,arr[i] - arr[i-1])

        return [minimum,maximum]
            
                

                
            
            
        
        