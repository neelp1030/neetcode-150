# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false
# two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values

# each recursive call on a node will return a boolean denoting whether two subtrees are equivalent
# cases are
# 1) if both p and q are null nodes, then return True
# 2) if either p or q are null node, then return False
# 3) both p and q are not null nodes, so first compare their values at the root, then recursively call on left and right subtrees of both

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# time complexity: O(n)
# space complexity: O(log(n))