# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left, q.left) and check(p.right, q.right)

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if check(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
