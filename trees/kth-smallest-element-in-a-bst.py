# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given the root of a BST, and an integer k, return the kth smallest value (1-indexed) in the tree
# a binary search tree satisfies the following constraints:
# the left subtree of every node contains only nodes with keys less than the node's key.
# the right subtree of every node contains only nodes with keys greater than the node's key.
# both the left and right subtrees are also binary search trees.

# we can use the idea of in-order traversal, which would traverse in order of lowest to highest value
# it's hard to do this
# let's try a dfs solution
# the base case is once k reaches 0, that means we have reached the kth-smallest value, so we return it
# another base case is if we encounter a null node, then we do nothing and simply return
# very useful to use nonlocal variables to pass common information between recursive function stack layers, like flags, etc.!

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        flag = False

        def dfs(root) -> int:

            nonlocal k
            nonlocal flag
            
            if not root:
                return 0

            val = dfs(root.left)

            if flag:
                return val
            
            if k == 1:
                flag = True
                return root.val

            k -= 1

            val = dfs(root.right)

            if flag:
                return val
            
            return root.val
        
        return dfs(root)

# time complexity: O(n)
# space complexity: O(log(n))