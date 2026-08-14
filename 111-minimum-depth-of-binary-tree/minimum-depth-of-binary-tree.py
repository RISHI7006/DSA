# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: 'Optional[TreeNode]') -> int:
        if root is None:
            return 0

        queue = deque([(root, 1)])  # (node, depth)

        while queue:
            node, depth = queue.popleft()

            # First leaf we find is guaranteed to be at the minimum depth
            if node.left is None and node.right is None:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0  # unreachable if root is not None