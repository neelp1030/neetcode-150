# given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i]
# each product is guaranteed to fit in a 32-bit integer
# solve it in O(n) time without using the division operation

# example 1
# input: nums = [1,2,4,6]
# prefix = [1,1,2,8]
# postfix = 1
# output: [48,24,12,8]

# example 2
# input: nums = [-1,0,1,2,3]
# output: [0,-6,0,0,0]

# output[i] will be the product of prefix[i] and postfix[i]
# prefix[i] is the product of all the preceding elements before index i in the input array
# postfix[i] is the product of all the following elements after index i in the input array

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= postfix
            postfix *= nums[i]
        
        return prefix
        
# time complexity: O(n)
# space complexity: O(n)