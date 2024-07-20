# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# given a binary tree root, return the level order traversal of it as a nested list
# where each sublist contains the values of nodes at a particular level in the tree, from left to right

# basically, this is just a standard BFS algorithm
# we need a queue, that we initialize with just the root
# then we run a while loop based on non-emptyness of the queue
# within the while loop, we run a for loop that pops each node from the queue one-by-one (basically the first level, then the next iteration of the while loop will do the next level, and so on)
# for each node that we pop, we will add back its left and right children to the queue if they are non-null

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        res = []
        q = collections.deque([root])
        
        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            res.append(level)
        
        return res

# time complexity: O(n)
# space complexity: O(n) <-- worst case the lowest level will have n/2 nodes