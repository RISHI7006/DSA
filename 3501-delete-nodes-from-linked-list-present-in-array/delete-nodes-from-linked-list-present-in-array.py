class Solution:
    def modifiedList(self, nums, head):
        remove = set(nums)

        while head and head.val in remove:
            head = head.next

        current = head

        while current and current.next:
            if current.next.val in remove:
                current.next = current.next.next
            else:
                current = current.next

        return head