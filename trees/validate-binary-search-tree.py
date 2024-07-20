# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given the root of a binary tree, return true if it is a valid BST, otherwise return false
# a valid BST satisfies the following constraints:
# the left subtree of every node contains only nodes with keys less than the node's key
# the right subtree of every node contains only nodes with keys greater than the node's key
# both the left and right subtrees are also BSTs

# basically, we can run a recursive DFS algorithm (top-down approach), since the root node will have 0 constraints on its value
# if at any point in the top-down approach we find that the current node does not satisfy constraints, we simply return false
# otherwise, we return the result of the recursive DFS calls on the node's left and right children
# base case is if we encounter a null node, in which case we simply return true
# to help us easily determine whether the current node satisfies constraints
# we will need to keep track of the upper and lower bounds for the current node, which we will pass in to our recursive DFS function

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lowerBound, upperBound) -> bool:
            if not root:
                return True
            
            if not (lowerBound < root.val < upperBound):
                return False

            return dfs(root.left, lowerBound, root.val) and dfs(root.right, root.val, upperBound)
        
        return dfs(root, float("-inf"), float("inf"))

# time complexity: O(n)
# space complexity: O(log(n))