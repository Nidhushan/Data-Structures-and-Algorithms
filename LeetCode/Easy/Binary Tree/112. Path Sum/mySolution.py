# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # DFS Iterative
        if not root:
            return False

        stack = [(root, root.val)]
        target = 0
        
        while stack:

            node, val = stack.pop()

            if not node.right and not node.left and val==targetSum:
                return True
            
            if node.right:
                stack.append((node.right, val+node.right.val))
            if node.left:
                stack.append((node.left, val+node.left.val))

        return False

        # Recursive:

        # if not root:
        #     return False
        # if not root.right and not root.left and root.val==targetSum:
        #     return True
        
        # targetSum -= root.val

        # return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        
            