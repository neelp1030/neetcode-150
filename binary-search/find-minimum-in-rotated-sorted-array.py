# you are given an array of length n which was originally sorted in ascending order
# it has now been rotated between 1 and n times
# for example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times
# [1,2,3,4,5,6] if it was rotated 6 times
# notice that rotating the array 4 times moves the last four elements of the array to the beginning
# rotating the array 6 times produces the original array
# assuming all elements in the rotated sorted array are unique, return the minimum element of this array
# a solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(logn) time?

# Example 1:
# Input: nums = [3,4,5,6,1,2]
# Output: 1

# Example 2:
# Input: nums = [4,5,0,1,2,3]
# Output: 0

# Example 3:
# Input: nums = [4,5,6,7]
# Output: 4

# we need some way of determining whether we need to look to the left or right side of our midpoint in each iteration
# after some thinking, we can observe that if our midpoint value < end value, then it means that the sequence is contiguous, so the minimum value would be in the left portion of the midpoint
# similarly, if our midpoint value > end value, then it means that the sequence is disconnected at some point on the right side, so the minimum value would be in the right portion of the midpoint
# we don't need to worry about the midpoint value = end value case, as we are guaranteed that the values in array are unique

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        curr_min = float("inf")
        
        while l <= r:
            m = l + ((r - l) // 2)
            curr_min = min(curr_min, nums[m])
            
            # right side has the min
            if nums[m] > nums[r]:
                l = m + 1
                
            # left side has the  min 
            else:
                r = m - 1
                
        return curr_min

# time complexity: O(logn)
# space complexity: O(1)