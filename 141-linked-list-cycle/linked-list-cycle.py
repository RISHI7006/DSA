# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: 'Optional[ListNode]') -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next        # moves 1 step
            fast = fast.next.next   # moves 2 steps

            if slow == fast:
                return True  # they met, cycle detected

        return False  # fast reached the end, no cycle
        