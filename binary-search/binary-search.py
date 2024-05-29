# you are given an array of distinct integers nums, sorted in ascending order, and an integer target
# implement a function to search for target within nums
# if it exists, then return its index, otherwise, return -1
# your solution must run in O(logn) time

# Example 1:
# Input: nums = [-1,0,2,4,6,8], target = 4
# Output: 3

# Example 2:
# Input: nums = [-1,0,2,4,6,8], target = 3
# Output: -1

# we can use a standard binary search algorithm here since the array is sorted
# we use two pointers l and r, initially set to the start and end of the array
# at each iteration of the algorithm, we take the midpoint of l and r and compare it to our target
# then we either return a result or change our l or r pointer to cut the problem space in half based on the midpoint value and the target
# if we are unable to find the target, then eventually the l and r pointer will be equal and the next iteration will cause l > r and the while loop will terminate
# ^ in which case we return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1

# time complexity: O(logn)
# space complexity: O(1)