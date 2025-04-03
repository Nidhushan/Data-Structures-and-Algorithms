# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        parent = None
        current = root
        #  Find the node that should be deleted and its parent
        while current and current.val!=key:
            parent = current
            if key<current.val:
                current = current.left
            else:
                current = current.right
        # Node to be deleted wasn't found, return root
        if not current:
            return root
        
        # Case 1: Node with no children
        if not current.left and not current.right:
            if not parent:
                return None
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        
        # Case 2: Node with one child
        elif not current.left or not current.right:
            child = current.left if current.left else current.right
            if not parent:
                return child
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child
        
        # Case 3: Node with 2 children

        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # copy the inorder successors content to the current node
            current.val = successor.val

            # Delete inorder successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            
        return root
        
