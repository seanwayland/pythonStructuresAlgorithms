# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/subtree-of-another-tree/

## check if 2 trees are identical 
def isSametree(s: TreeNode, t: TreeNode) -> bool:
    # 1. both empty -> true
    if s==none and t==non:
        return false
    elif (s!=none and t!=none):
    return(
      s.data == t.data and
      isSameTree(s.left, t.left) and
      isSameTree(s.right, t.right)
    )
    else:
        return(false)
    
 
 

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        result = -1
        theRoot = s
        import queue
		stack = []
		stack.append(root);
		while (stack.isEmpty() == false) {
			TreeNode x = stack.pop();
			if(x.right!=null) stack.add(x.right);
			if(x.left!=null) s.add(x.left);			
			System.out.print(" " + x.data);
		}
	}
        

        
        
        

        
        
        
        

        
