# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # result = []

        # def dfs(node, depth):
        #     if node is None:
        #         return None
        #     if len(result) == depth:
        #         result.append([])
            
        #     result[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        
        # dfs(node = root, depth = 0)

        # return result

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            level = []

            # Number of nodes in CURRENT LEVEL
            level_size = len(queue)

            for _ in range(level_size):
                
                # Visit Current Node
                node = queue.popleft()

                # Process Current Node
                level.append(node.val)

                # Add Childrens for NEXT Level
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            result.append(level)
        
        return result


        