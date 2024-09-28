# there is an undirected graph with n nodes
# there is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph
# the nodes are numbered from 0 to n - 1
# return the total number of connected components in that graph

# this one is easy
# we just run dfs on each node one by one, keep track of a visited set, and skip nodes that have already been visited, increment result by 1 for each dfs call
# we will need to populate an adjacency list for this as well, since we are given a list of edges
# keep in mind that this is an undirected graph
# do we need the prev parameter in the dfs function for this undirected graph?
# dont think so, because we will not be looking to detect a cycle specifically and we just skip a node if it has already been visited

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjListMap = {i: [] for i in range(n)}
        visited = set()
        numConnectedComponents = 0

        for n1, n2 in edges:
            adjListMap[n1].append(n2)
            adjListMap[n2].append(n1)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in adjListMap[node]:
                dfs(n)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                numConnectedComponents += 1
        
        return numConnectedComponents

# time complexity: O(n + p)
# space complexity: O(n)