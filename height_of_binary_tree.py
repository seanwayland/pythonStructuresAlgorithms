class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_height = 1 + self.maxDepth(root.left)
        right_height = 1 + self.maxDepth(root.right)
        return max(left_height , right_height)
        
