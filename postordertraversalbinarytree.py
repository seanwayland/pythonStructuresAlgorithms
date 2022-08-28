    class Solution:
      def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)
        return res
