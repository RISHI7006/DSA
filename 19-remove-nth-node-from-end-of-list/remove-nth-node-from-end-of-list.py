# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: 'Optional[ListNode]', n: int) -> 'Optional[ListNode]':
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Advance fast n+1 steps ahead so slow ends up right before target
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast hits the end
        while fast:
            fast = fast.next
            slow = slow.next

        # slow is now just before the node to remove
        slow.next = slow.next.next

        return dummy.next