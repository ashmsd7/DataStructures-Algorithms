# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head

            while curr:
                upcoming = curr.next
                curr.next = prev
                prev = curr
                curr = upcoming #Yay

            return prev    
        
        head = reverse(head)

        curr = head
        max_val = curr.val
        
        while curr.next:
            if curr.next.val < max_val :
                curr.next = curr.next.next
            else:
                max_val = curr.next.val
                curr = curr.next

        return reverse(head)            

        