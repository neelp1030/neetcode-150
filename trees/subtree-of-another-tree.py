# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given the roots of two binary trees root and subRoot
# return true if there is a subtree of root with the same structure of subRoot and false otherwise
# a subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants
# the tree tree could also be considered as a subtree of itself

# we will use a helper recursive function called isSameTree which will take two trees and determine if they are the same
# cases are
# 1) if subRoot is null node, then return True
# 2) if root is null node (and subRoot is not null node), then return False
# 3) if both root and subRoot are not null nodes, then return isSameTree(p, q) or isSubTree(p.left, q) or isSubTree(p.right, q)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

# time complexity: O(n * m)
# space complexity: O(log(n) + O(log(m)))