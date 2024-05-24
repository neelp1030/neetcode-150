# given an integer array nums and an integer k, return the k most frequent elements within the array
# the test cases are generated such that the answer is always unique
# you may return the output in any order

# example 1
# input: nums = [1,2,2,3,3,3], k = 2
# output: [2,3]

# example 2
# input: nums = [7,7], k = 1
# output: [7]

# we could use a heap, but in this case, we can actually do it more optimally using bucket sort
# first, we do a one-pass through the array and generate a hashmap representing the frequency of values in the array
# then, we create a fixed-size array of same length, where an element at index i will be a list of all values with frequency i, this can also be populated in one-pass
# finally, we just have to fetch the k most frequent elements from this array, by starting at the last index and exhausting all elements in the list and moving backwards until we reach k elements or we finish the array

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valFreq = {}

        for num in nums:
            valFreq[num] = valFreq.get(num, 0) + 1
        
        freqValues = [[] for i in range(len(nums))]

        for val, freq in valFreq.items():
            freqValues[freq - 1].append(val)
        
        res = []

        for i in range(len(freqValues) - 1, -1, -1):
            for val in freqValues[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return res

# time complexity: O(n)
# space complexity: O(n)