# you are given an array of integers stones where stones[i] represents the weight of the ith stone
# we want to run a simulation on the stones as follows:
# at each step, we choose the two heaviest stones, with weight x and y and smash them together
# if x == y, both stones are destroyed
# if x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x
# continue the simulation until there is no more than one stone remaining
# return the weight of the last remaining stone or return 0 if none remain

# we will use a maxHeap since we repeatedly will need the two largest stones and the list is volatile throughout the procedure
# we will repeatedly pop the largest two stones and add a stone back depending on the weights
# this will repeat until the length of the maxHeap becomes <= 1, at which point we will terminate
# and return either the weight of the last remaining stone or return 0 if none remain

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap) * -1
            second = heapq.heappop(maxHeap) * -1

            if first > second:
                heapq.heappush(maxHeap, (first - second) * -1)
        
        return (maxHeap[0] * -1) if len(maxHeap) == 1 else 0

# time complexity: O(nlog(n))
# space complexity: O(n)