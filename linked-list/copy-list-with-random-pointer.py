"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# you are given the head of a linked list of length n
# unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null
# create a deep copy of the list
# the deep copy should consist of exactly n new nodes, each including:
# the original value val of the copied node
# a next pointer to the new node corresponding to the next pointer of the original node
# a random pointer to the new node corresponding to the random pointer of the original node
# note: none of the pointers in the new list should point to nodes in the original list
# return the head of the copied linked list
# in the examples, the linked list is represented as a list of n nodes
# each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node

# we can create a map to associate each original node (key) with its new node (value)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head

        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]

# time complexity: O(n)
# space complexity: O(n)