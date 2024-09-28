# given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes)
# write a function to check whether these edges make up a valid tree

# the big idea behind this problem is what constitutes a valid tree based on an undirected graph
# a tree is connected (meaning that all other nodes must be visitable from any node in the graph)
# and the graph does not have a cycle
# given this, we can simply run a dfs on any node (let's just do node 0)
# keep track of a visited set
# if we detect a cycle, we return false
# if not, then we check whether len(visited) == n, and return true or false based on that

# we are given edges for the graph, so let's construct an adjacency list based on this to help us traverse the graph

# IMPORTANT: during the dfs algorithm, because the graph is undirected, we need to make sure to restrict a direct loop on the edge between two nodes (otherwise we falsely detect a cycle in this context), so we need to track previousNode during the dfs algorithm

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjListMap = {i: [] for i in range(n)}
        visited = set()

        for n1, n2 in edges:
            adjListMap[n1].append(n2)
            adjListMap[n2].append(n1)
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for n in adjListMap[node]:
                if n == prev:
                    continue

                if not dfs(n, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

# time complexity: O(n + p)
# space complexity: O(n)