# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point = head
        while point and point.next:
            if point.val == point.next.val:
                point.next = point.next.next
            else:
                point = point.next
        
        return head


        