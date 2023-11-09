# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if root is None:
                return True

            left = depth(root.left)
            right = depth(root.right)
            if left is False or right is False or abs(left - right) > 1:
                return False
            return max(left, right) + 1

        return depth(root)
