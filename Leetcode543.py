# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            nonlocal cur_max
            if root is None:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            cur_max = max(cur_max, left + right)
            return 1 + max(left, right)

        cur_max = 0
        depth(root)
        return cur_max
