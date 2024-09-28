# you are given an array nums of integers, which may contain duplicates
# return all possible subsets
# the solution must not contain duplicate subsets
# you may return the solution in any order

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # branch 1: include nums[i], then we move onto next index
            subset.append(nums[i])
            dfs(i + 1)

            # branch 2: don't include nums[i], then we increment index until nums[i] != nums[i + 1]
            subset.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)
        
        dfs(0)

        return res