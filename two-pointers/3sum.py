# given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j, and k are all distinct.
# the output should not contain any duplicate triplets
# you may return the output and the triplets in any order

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# sorted: nums = [-1,-1,0,1,2,4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# since we know that the optimal solution will still be quite slow, it is worth sorting the array at the very start so we can use more efficient algorithms
# first, we sort the array
# we do one loop through the array

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            # skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            # two pointer technique on subarray
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

# time complexity: O(n^2)
# space complexity: O(1)