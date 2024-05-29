# you are given an array of length n which was originally sorted in ascending order
# it has now been rotated between 1 and n times
# for example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times
# [1,2,3,4,5,6] if it was rotated 6 times
# given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present
# you may assume all elements in the sorted rotated array nums are unique
# a solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(logn) time?

# Example 1:
# Input: nums = [3,4,5,6,1,2], target = 1
# Output: 4

# Example 2:
# Input: nums = [3,5,6,0,1,2], target = 4
# Output: -1

# let's say our midpoint is 5, target is 1, start is 3, end is 2, which half do we continue searching in?
# since our midpoint > end, we know we are in the left sorted portion of the rotated array
# similarly, if our midpoint < end, we know we are in the right sorted portion of the rotated array
# if we are in the left sorted portion, then there are two cases
# if start < target < midpoint, then we should search in the left portion of the midpoint
# otherwise, we should search in the right portion of the midpoint
# similarly, if we are in the right sorted portion, then there are also two cases
# if midpoint < target < end, then we should search in the right portion of the midpoint
# otherwise, we should search in the left portion of the midpoint

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == nums[m]:
                return m

            # left sorted portion
            if nums[m] > nums[r]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # right sorted portion
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

# time complexity: O(logn)
# space complexity: O(1)