# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p1 = head
        st = []
        while p1:
            st.append(p1.val)
            p1=p1.next
        return st == st[::-1]