# given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j
# you may assume that every input has exactly one pair of indices i and j that satisfy the condition
# return the answer with the smaller index first

# example 1
# input: nums = [3, 4, 5, 6], target = 7
# output: [0, 1]

# example 2
# input: nums = [4, 5, 6], target = 10
# output: [0, 2]

# example 3
# input: nums = [5, 5], target = 10
# output: [0, 1]

# example 4
# input: nums = [5, 5, 7], target = 12 <-- not possible!

# we can do this in one-pass by keeping track of the values encountered and their indices in a hashmap, with key being the value and value being the index
# what if there are multiple of the same value in the nums array? it's fine as if that ends up being the answer, then we will automatically return the first possible combination and our hashmap will not need to track duplicate values

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevEncountered = {}

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in prevEncountered:
                return [prevEncountered[remainder], i]

            prevEncountered[num] = i
        
        return []

# time complexity: O(n)
# space complexity: O(n)