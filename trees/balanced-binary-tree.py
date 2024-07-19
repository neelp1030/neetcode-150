# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given a binary tree, return true if it is height-balanced and false otherwise
# a height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1

# each recursive call on a node will return a tuple of [balanced, height]
# where balanced is a boolean denoting whether the subtree starting at root node is balanced or not
# where height is the height of the subtree starting at root node
# base case is null node, where we return [True, 0]

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root) -> [bool, int]:
            if not root:
                return [True, 0]
            
            balancedLeft, heightLeft = dfs(root.left)
            balancedRight, heightRight = dfs(root.right)

            balanced = balancedLeft and balancedRight and (abs(heightLeft - heightRight) <= 1)
            height = 1 + max(heightLeft, heightRight)

            return [balanced, height]
        
        res, _ = dfs(root)

        return res

# time complexity: O(n)
# space complexity: O(log(n))