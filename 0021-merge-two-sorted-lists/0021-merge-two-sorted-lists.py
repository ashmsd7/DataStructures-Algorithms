# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left_p = list1
        right_p = list2

        dummy = ListNode(0)
        tail = dummy

        while left_p and right_p:
            if left_p.val <= right_p.val:
                tail.next = left_p
                left_p = left_p.next
            else:
                tail.next = right_p
                right_p = right_p.next
            tail = tail.next
        
        if left_p:
            tail.next = left_p
        if right_p:
            tail.next = right_p
        return dummy.next
        

        
    