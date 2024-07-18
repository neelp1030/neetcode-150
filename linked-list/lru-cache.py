# implement the least recently used (LRU) cache class LRUCache
# the class should support the following operations
# LRUCache(int capacity) - initialize the LRU cache of size capacity
# int get(int key) - return the value corresponding to the key if the key exists, otherwise return -1
# void put(int key, int value) - update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
# a key is considered used if a get or a put operation is called on it
# ensure that get and put each run in O(1) average time complexity

# for the cache functionality in general, we will need to use a map to store the key-value pairs
# additionally, to implement the LRU functionality, we will need to maintain a linked list where the first node will be the oldest entry and the last node will be the newest entry

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        # dummy start and end node for the linked list, initially they are the only two nodes in the list
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]