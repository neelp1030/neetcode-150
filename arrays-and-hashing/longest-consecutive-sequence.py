# given an array of integers nums, return the length of the longest consecutive sequence of elements
# a consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element
# you must write an algorithm that runs in O(n) time

# Example 1:
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7

# we can populate a hashset of values by doing a one-pass through the array
# then, we can do a second pass through the array. this time, for each value, we will check if it is the starting point of a sequence (does the integer right before it exist in our hashset?)
# if it is not the start of a sequence, we skip it and move onto next element
# if it is the start of a sequence, we track the size of the sequence and keep incrementing until the value no longer exists in our hashset, that will be the size of the sequence starting at that value
# we need to track the maximum sequence size
# note that the algorithm will only visit each element in the array a max of two times each, so O(n) time

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()

        for num in nums:
            mySet.add(num)
        
        maxConsecutiveSeqLen = 0

        for num in nums:
            if num - 1 not in mySet:
                currConsecutiveSeqLen = 0

                while num in mySet:
                    currConsecutiveSeqLen += 1
                    num += 1
                
                maxConsecutiveSeqLen = max(maxConsecutiveSeqLen, currConsecutiveSeqLen)

        return maxConsecutiveSeqLen

# time complexity: O(n)
# space complexity: O(n)