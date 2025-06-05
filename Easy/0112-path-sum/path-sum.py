# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Empty Tree Condition or Reached Null Node while recursion.
        # This means no path is available.
        if not root:
            return False
        
        # Leaf Node Check
        if not root.left and not root.right:
            # If the current value is same as remaining target then path found else not.
            return targetSum - root.val == 0
        
        # Update Target Sum Before Recusive Check.
        # Subtracting the node value from target before going down the path.
        targetSum -= root.val

        # Recursively Check on both left or right whichever leads to target sum.
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right, targetSum)