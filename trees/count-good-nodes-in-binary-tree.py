# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x
# given the root of a binary tree root, return the number of good nodes within the tree

# we can do a recursive DFS algorithm for this, where each node will recursively call on its children
# the recursive DFS function will return the total number of good nodes in the subtree with root node
# to help us easily determine whether the current node is a good node, we will also pass in an extra parameter to our recursive DFS function
# this will be the greatest value encountered so far, so we can just compare this to root.val to determine if root node is a good node or not
# base case is null node, where we simply return 0

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, highest) -> int:
            if not root:
                return 0
            
            if root.val >= highest:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, highest) + dfs(root.right, highest)
        
        return dfs(root, root.val)

# time complexity: O(n)
# space complexity: O(log(n))