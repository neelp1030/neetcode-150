# given an array of integers numbers that is sorted in non-decreasing order
# return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2.
# note that index1 and index2 cannot be equal, therefore you may not use the same element twice
# there will always be exactly one valid solution
# your solution must use O(1) space

# Example 1:
# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]
# Explanation:
# The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

# standard two pointer technique

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l + 1, r + 1]
            elif sum < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]

# time complexity: O(n), at each step of the algorithm, we converge by one element towards the middle
# space complexity: O(1)