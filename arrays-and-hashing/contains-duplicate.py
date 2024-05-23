# given an integer array nums, return true if any value appears more than once in the array, otherwise return false

# example 1
# input: nums = [1, 2, 3, 3]
# output: true

# example 2
# input: nums = [1, 2, 3, 4]
# output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()

        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)