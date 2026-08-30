# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Recursion -----

        # if root is None:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Depth First Search

        # result = 0

        # stack = [[root, 1]]

        # while stack:

        #     node, depth = stack.pop()

        #     if node:
        #         result = max(result, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])
            
        # return result

        # Breadth First Search

        if root is None:
            return 0

        queue = deque([root])

        max_level = 0

        while queue:

            level_size = len(queue)

            for _ in range(level_size):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            max_level += 1
        
        return max_level
    

    
                

            
                


        