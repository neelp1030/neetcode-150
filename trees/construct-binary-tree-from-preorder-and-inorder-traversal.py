# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# you are given two integer arrays preorder and inorder
# preorder is the preorder traversal of a binary tree
# inorder is the inorder traversal of the same tree
# both arrays are of the same size and consist of unique values
# rebuild the binary tree from the preorder and inorder traversals and return its root

# at each step of the way, we know that the preorder list's first element is our root of the subtree remaining to be built
# given the root, we find its positioning in the inorder list
# everything to the left of that in the inorder list is the left subtree
# everything to the right of that in the inorder list is the right subtree
# so at each step of the recursive DFS algorithm, we create the root node first
# then, we assign root.left to buildTree(preorder[1:index + 1], inorder[:index])
# then, we assign root.right to buildTree(preorder[index + 1:], inorder[index + 1:])
# if at any point, preorder and inorder lists are empty (if one is empty, the other must necessarily also be empty), then we simply return

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])

        return root

# time complexity: O(n)
# space complexity: O(log(n))