# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given the root of a binary tree, return its depth
# the depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node

# base case: null node -> depth of 0
# otherwise, the node's depth is 1 + max(depth(left), depth(right))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# time complexity: O(n)
# space complexity: O(log(n))