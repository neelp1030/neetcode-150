# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree
# the path does not necessarily have to pass through the root
# the length of a path between two nodes in a binary tree is the number of edges between the nodes
# given the root of a binary tree root, return the diameter of the tree

# each call to the recursive function for a given node will return a tuple of [maxDiameter, height]
# where maxDiameter is the max diameter in that subtree starting at that node as the root (the diameter does not necessarily have to pass through the root)
# where height is the height of the node
# the base case is null node, where we return [0, 0]

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root) -> [int, int]:
        
            if not root:
                return [0, 0]
            
            # the max diameter of the subtree starting at root will be the max of
            # 1) height(root.left) + height(root.right) + 2 edges
            # 2) maxDiameter(root.left)
            # 3) maxDiameter(root.right)

            maxDiameterLeft, heightLeft = dfs(root.left)
            maxDiameterRight, heightRight = dfs(root.right)

            return [max(heightLeft + heightRight, maxDiameterLeft, maxDiameterRight), 1 + max(heightLeft, heightRight)]
        
        res, _ = dfs(root)

        return res

# time complexity: O(n)
# space complexity: O(log(n))