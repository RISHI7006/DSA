# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: 'Optional[TreeNode]') -> bool:
        def height(node: 'Optional[TreeNode]') -> int:
            if node is None:
                return 0

            left_h = height(node.left)
            if left_h == -1:
                return -1  # left subtree already unbalanced, propagate up

            right_h = height(node.right)
            if right_h == -1:
                return -1  # right subtree already unbalanced, propagate up

            if abs(left_h - right_h) > 1:
                return -1  # this node is unbalanced

            return max(left_h, right_h) + 1

        return height(root) != -1