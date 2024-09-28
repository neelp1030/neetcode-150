# given an array nums of unique integers, return all possible subsets of nums
# the solution set must not contain duplicate subsets
# you may return the solution in any order

# solving this problem intuitively is as follows
# for each element in the list, we have the option of either including it or not including it
# we can process all the possible subsets using this logic, as a decision tree
# we will use a DFS algorithm to discover all possible subsets
# the DFS method will have an index (of the nums list) that we have to branch off from (whether we include that element or not)
# the base case is if the index == len(nums), then we have arrived at a final possible subset, and we add it to our final result list

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # branch 1: include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # branch 2: don't include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)

        return res

# time complexity: O(2^n)
# space complexity: O(2^n)