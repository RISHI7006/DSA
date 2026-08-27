# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: 'ListNode', headB: 'ListNode') -> 'Optional[ListNode]':
        if not headA or not headB:
            return None

        pointerA = headA
        pointerB = headB

        # When one pointer reaches the end, redirect it to the other list's head
        # This ensures both pointers travel the same total distance
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA  # either the intersection node, or None if no intersection
        