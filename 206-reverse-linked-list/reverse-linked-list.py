# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: 'Optional[ListNode]') -> 'Optional[ListNode]':
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # save the next node before we lose it
            curr.next = prev       # reverse the link
            prev = curr            # move prev forward
            curr = next_node       # move curr forward

        return prev  # prev is now the new head