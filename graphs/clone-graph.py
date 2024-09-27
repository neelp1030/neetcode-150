# given a node in a connected undirected graph, return a deep copy of the graph
# each node in the graph contains an integer value and a list of its neighbours

# the graph is shown in the test cases as an adjacency list
# an adjacency list is a mapping of nodes to lists, used to represent a finite graph
# each list describes the set of neighbours of a node in the graph
# for simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph
# the index of each node within the adjacency list is the same as the node's value (1-indexed)

# the input node will always be the first node in the graph, and have 1 as the value

# we will use a map to associate old graph node to new graph node
# we can do the entire cloning process in a single dfs pass
# each dfs call on a node will return the cloned copy of that node
# it will create a copy for the node if it doesn't already exist as well as populate its neighbors using recursive dfs calls

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNewMap = {}
        
        def dfs(node):
            if node in oldToNewMap:
                return oldToNewMap[node]
            
            copy = Node(node.val)
            oldToNewMap[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node) if node else None