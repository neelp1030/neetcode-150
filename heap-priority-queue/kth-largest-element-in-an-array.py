# given an unsorted array of integers nums and an integer k, return the kth largest element in the array
# by kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element
# follow-up: can you solve it without sorting?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]

# time complexity: O(n + klog(n))
# space complexity: O(1)