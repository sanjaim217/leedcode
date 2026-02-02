# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # base case
        if not head or not head.next:
            return head
        
        # recursive case
        _next = head.next
        head.next = self.swapPairs(_next.next)
        _next.next = head
        
        return _next  