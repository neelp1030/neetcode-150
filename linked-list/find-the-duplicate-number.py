# you are given an array of integers nums containing n + 1 integers
# each integer in nums is in the range [1, n] inclusive
# every integer appears exactly once, except for one integer which appears two or more times
# return the integer that appears more than once

# the solution uses the floyd's algorithm since we know there will be a cycle if we follow the algorithm
# using the point where the slow and fast pointer meet, we can backtrack to find the node where the cycle first starts
# this problem can be thought of as a linked list cycle problem since all integers are unique except one
# and each integer maps to another integer in the list

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow

# time complexity: O(n)
# space complexity: O(1)