from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        queue = deque()

        if root:
            queue.appendleft(root)
        while len(queue) > 0:
            level_order = []
            for i in range(len(queue)):
                node = queue.pop()
                level_order.append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            order.append(level_order)
        return order




