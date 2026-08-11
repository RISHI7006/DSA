# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: 'Optional[TreeNode]') -> bool:
        def isMirror(t1: 'Optional[TreeNode]', t2: 'Optional[TreeNode]') -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.val == t2.val
                    and isMirror(t1.left, t2.right)   # outer pair
                    and isMirror(t1.right, t2.left))  # inner pair

        return isMirror(root.left, root.right) if root else True