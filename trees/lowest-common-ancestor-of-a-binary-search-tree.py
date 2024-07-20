# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given a BST where all node values are unique, and two nodes from the tree p and q
# return the lowest common ancestor (LCA) of the two nodes
# the LCA between two nodes p and q is the lowest node in a tree T such that both p and q are descendants
# the ancestor is allowed to be a descendant of itself

# we will start at the root of the tree and use a recursive dfs solution
# a recursive dfs call to a node will either return itself (meaning that it is the LCA), or it will recursively call on either its left or right child
# since p and q are guaranteed to exist in the BST, then the first case discussed is our base case
# the base case happens if root.val is in between p.val and q.val (inclusive)
# otherwise, we can find a lower common ancestor based on whether root.val is higher or lower (non-inclusive) than both p.val and q.val

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# time complexity: O(log(n)) <-- we only visit at max one node from each level
# space complexity: O(log(n))