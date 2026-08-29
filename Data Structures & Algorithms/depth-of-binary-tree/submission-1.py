# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # DFS

        # stack = [[root, 1]]
        # max_depth = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         max_depth = max(depth, max_depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
            
        # return max_depth

        # BFS

        q = deque()

        if not root:
            return 0
        
        q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            level += 1
        
        return level
                
    

        