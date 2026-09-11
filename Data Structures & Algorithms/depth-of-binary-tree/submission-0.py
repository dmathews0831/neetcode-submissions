# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def parse(curr) -> int:
            right, left = 0, 0
            if curr.right:
                right = parse(curr.right)
            if curr.left:
                left = parse(curr.left)
            return 1 + max(right, left)
        return parse(root) if root else 0

            