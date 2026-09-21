# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Dummy node simplifies edge cases where head itself must be removed
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                # Skip curr by linking prev directly to curr.next
                prev.next = curr.next
            else:
                # Only advance prev when we keep the current node
                prev = curr
            curr = curr.next
        
        return dummy.next