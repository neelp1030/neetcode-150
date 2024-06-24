# you are given an integer array heights where heights[i] represents the height of the ith bar
# you may choose any two bars to form a container
# return the maximum amount of water a container can store

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res

# time complexity: O(n), at every step of the iteration we converge towards the middle by one element
# space complexity: O(1)