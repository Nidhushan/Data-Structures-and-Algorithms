# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # BFS Iterative:
        
        queue = deque([root])
        parent = {root: None}
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left] = node
            if node.right:
                queue.append(node.right)
                parent[node.right] = node
            
            if p in parent and q in parent:
                break

        # # Less Intuitive implementation but takes lesser space:

        # pointer1, pointer2 = p, q

        # # Move both pointers up until they meet:
        # while pointer1 != pointer2:
        #     pointer1 = parent[pointer1] if pointer1 else q
        #     pointer2 = parent[pointer2] if pointer2 else p

        # return pointer1

        # Easier more intuitive way to do above:

        ancestor = set()        
        while p:
            ancestor.add(p)
            p = parent[p]
        
        while q:
            if q in ancestor:
                return q
            q = parent[q]
        

        # DFS Recursive Method:

        # if root == None or root == p or root == q: return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left!=None and right!=None:
        #     return root
        # if left!=None:
        #     return left
        # return right