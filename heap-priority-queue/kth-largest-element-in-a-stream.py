# design a class to find the kth largest integer in a stream of values, including duplicates
# e.g. the 2nd largest from [1,2,3,3] is 3
# the stream is not necessarily sorted
# implement the following methods
# constructor(int k, int[] nums) - initializes the object given an integer k and the stream of integers nums
# int add(int val) - adds the integer val to the stream and returns the kth largest integer in the stream

# the idea is that we wish to consistently be able to determine the kth largest integer in a stream of values
# if it was just a one time operation, then we could just sort the array and find the kth largest integer or something
# but if we need to find it several times, we would have to constantly resort the array, which is inefficient
# the solution is to use a minHeap with the k largest integers
# heapify takes O(n) time
# heappush/heappop take O(log(n)) time

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # at this point, we will have the k largest integers in our minHeap, and the front of the minHeap will be the kth largest integer

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0] # the front of the minHeap is the kth largest integer