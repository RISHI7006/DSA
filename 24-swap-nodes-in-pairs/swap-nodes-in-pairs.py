class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next   # 1 -> 3
            second.next = first        # 2 -> 1
            prev.next = second         # dummy -> 2

            prev = first               # move to the end of the swapped pair

        return dummy.next