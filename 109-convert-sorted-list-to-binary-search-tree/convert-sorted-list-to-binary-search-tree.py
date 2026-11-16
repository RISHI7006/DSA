class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        cur = head

        def build(l, r):
            nonlocal cur
            if l > r:
                return None
            mid = (l + r) // 2
            left = build(l, mid - 1)      # 1. build left subtree first
            root = TreeNode(cur.val)      # 2. current list node is the root
            cur = cur.next
            root.left = left
            root.right = build(mid + 1, r)  # 3. then the right subtree
            return root

        return build(0, n - 1)