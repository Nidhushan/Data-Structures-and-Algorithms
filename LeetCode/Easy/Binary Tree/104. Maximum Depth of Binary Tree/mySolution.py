# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Iterative Solution(While only):
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        
        return level

        # Recursive solution:

        # if not root:
        #     return 0
        
        # return max(self.maxDepth(root.left), self.maxDepth(root.right))+1