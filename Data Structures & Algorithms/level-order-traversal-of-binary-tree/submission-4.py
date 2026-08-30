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

        #     if not node:
        #         return None
            
        #     if len(result) == depth:
        #         result.append([])
            
        #     result[depth].append(node.val)
        #     dfs(node.left, depth + 1)
        #     dfs(node.right, depth + 1)
        

        # dfs(root, 0)

        # return result


        if root is None:
            return []


        result = []

        queue = deque([root])

        while queue:
            
            level = []

            level_size = len(queue)
            
            for _ in range(level_size):

                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result



