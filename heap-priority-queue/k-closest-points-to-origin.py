# you are given a 2D array points where points[i] = [xi, yi] represents the coordinates of a point on an XY axis plane
# you are also given an integer k
# return the k closest points to the origin (0,0)
# the distance between two points is defined as the Euclidean distance sqrt((x1 - x2)^2 + (y1 - y2)^2)
# you may return the answer in any order

# since we just need to find the k closest points given some metric in a fixed list and not a stream
# we can simply use a minHeap and pop the k smallest elements to get our answer
# we also don't need to do the sqrt for the Euclidean distance as it won't affect the ordering of the elements

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            euclideanDist = (x ** 2) + (y ** 2)
            minHeap.append((euclideanDist, x, y))
        
        heapq.heapify(minHeap)
        
        res = []

        for i in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        
        return res

# time complexity: O(n + klog(n))
# space complexity: O(n)