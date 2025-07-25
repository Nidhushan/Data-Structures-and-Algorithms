# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Iterative BFS:
        # if not nums:
        #     return None
        
        # n = len(nums)
        # mid = n//2
        # root = TreeNode(nums[mid])

        # q = deque()
        # q.append((root, 0, mid-1))
        # q.append((root, mid+1, n-1))

        # while q:
        #     parent, left, right = q.popleft()

        #     if left<=right:
        #         mid = (left+right)//2

        #         child = TreeNode(nums[mid])
        #         if nums[mid] < parent.val:
        #             parent.left = child
        #         else:
        #             parent.right = child
        #         q.append((child, left, mid-1))
        #         q.append((child, mid+1, right))
        # return root
        # Recursive but better time and space due to using indices

        def BSTify(left, right):
            if left>right:
                return None
            
            mid = (left+right)//2
            node = TreeNode(nums[mid])
            node.left = BSTify(left, mid-1)
            node.right = BSTify(mid+1, right)

            return node
        return BSTify(0, len(nums)-1)
        
        # Recursive:
        # if not nums:
        #     return None
        
        # mid = len(nums)//2

        # root = TreeNode(nums[mid])
        # root.left = self.sortedArrayToBST(nums[:mid])
        # root.right = self.sortedArrayToBST(nums[mid+1:])

        # return root