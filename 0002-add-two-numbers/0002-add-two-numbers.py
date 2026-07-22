# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            tail.next = ListNode(x + y + carry)
            carry = 0
            if tail.next.val >=10:
                tail.next.val = tail.next.val - 10
                carry = 1
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            tail = tail.next
        if carry > 0:
            tail.next = ListNode(carry)
        return dummy.next