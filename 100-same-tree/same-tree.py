# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: 'Optional[TreeNode]', q: 'Optional[TreeNode]') -> bool:
        # Both empty -> identical (trivially)
        if p is None and q is None:
            return True

        # One empty, one not -> structurally different
        if p is None or q is None:
            return False

        # Both non-empty: check value + recurse into both subtrees
        return (p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))