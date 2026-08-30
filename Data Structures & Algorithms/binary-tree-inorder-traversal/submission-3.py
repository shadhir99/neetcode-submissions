# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # res = []

        # def inorder(node):
        #     if node is None:
        #         return None
            
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        
        # inorder(root)
        # return res

        result = []

        stack = []

        curr = root

        while stack or curr:

            # Go until last left node while stacking right nodes
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process Root Node
            curr = stack.pop()
            result.append(curr.val)

            # Move to Right
            curr = curr.right
        
        return result
            



        



        
        