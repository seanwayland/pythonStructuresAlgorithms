class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root is None : return None        
        if root in nodes: return root        
        L, R = self.lowestCommonAncestor(root.left, nodes), self.lowestCommonAncestor(root.right, nodes)        
        if L and R: return root        
        if L: return L        
        return R
