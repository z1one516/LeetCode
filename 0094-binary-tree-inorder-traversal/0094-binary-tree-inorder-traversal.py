# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 중위순회 : L -> root -> R
            stack = []
            result = []
            
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                result.append(root.val)
                root = root.right
                
            return result
#     # DFS preorder : root -> left -> right
#     def preorder(root):
#         return [root.val] + preorder(root.left) + preorder(root.right) if root else []
    
#     # DFS inorder : left -> root -> right
#     def inorder(root):
#         return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    
#     # DFS postorder : left -> right -> root
#     def postorder(root):
#         return postorder(root.left) + postorder(root.right) + [root.val] if root else []