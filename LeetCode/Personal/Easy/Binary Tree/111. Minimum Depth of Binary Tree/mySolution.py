# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative Solution(For Loop):

        # queue = deque([root])
        # result = 0
        # if not root:
        #     return 0
        # while deque:
        #     result+=1
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #         if not (node.left or node.right):
        #             return result

        # Iterative Solution(While only):
        queue = deque([(root, 1)])
        if not root:
            return 0
        while queue:
            node, level = queue.popleft()
            if not node.left and not node.right:
                return level
            
            if node.left: queue.append((node.left, level+1))
            if node.right: queue.append((node.right, level+1))
        
        return 0

        # Recursive Solution:

        # if not root:
        #     return 0
        
        # if None in [root.left, root.right]:
        #     return max(self.minDepth(root.left), self.minDepth(root.right))+1
        # else:
        #     return min(self.minDepth(root.left), self.minDepth(root.right))+1


