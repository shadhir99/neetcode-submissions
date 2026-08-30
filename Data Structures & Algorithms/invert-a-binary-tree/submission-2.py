# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion
        
        # if not root:
        #     return None
        
        # root.right, root.left = root.left, root.right

        # self.invertTree(root.left)
        # self.invertTree(root.right)
    
        # return root

        # DFS

        # if not root:
        #     return None

        # stack = [root]

        # while stack:
        #     node = stack.pop()

        #     if node:
        #         node.right, node.left = node.left, node.right
        #         stack.append(node.left)
        #         stack.append(node.right)
            
        # return root

        # BFS

        if not root:
            return None

        queue = deque([root])

        while queue:

            node = queue.popleft()

            node.right, node.left = node.left, node.right

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root

        