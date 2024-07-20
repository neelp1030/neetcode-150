# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# you are given the root of a binary tree
# return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom

# basically, we are just doing a BFS traversal (level by level), but in each level we are only adding the last popped node's value to the result list

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = []
        q = collections.deque([root])

        while q:
            lastNodeOfLevel = None

            for i in range(len(q)):
                lastNodeOfLevel = q.popleft()

                if lastNodeOfLevel.left:
                    q.append(lastNodeOfLevel.left)
                
                if lastNodeOfLevel.right:
                    q.append(lastNodeOfLevel.right)
                
            res.append(lastNodeOfLevel.val)
        
        return res

# time complexity: O(n)
# space complexity: O(n) <-- worst case the lowest level will have n/2 nodes