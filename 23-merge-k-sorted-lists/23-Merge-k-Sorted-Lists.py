class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(a, b):
            dummy = ListNode(0)
            tail = dummy
            while a and b:
                if a.val <= b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
                tail = tail.next
            tail.next = a or b
            return dummy.next

        step = 1
        n = len(lists)
        while step < n:
            for i in range(0, n - step, step * 2):
                lists[i] = merge(lists[i], lists[i + step])
            step *= 2

        return lists[0]