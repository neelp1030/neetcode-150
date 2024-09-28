# you are given an array of distinct integers nums and a target integer target
# your task is to return a list of all unique combinations of nums where the chosen numbers sum to target
# the same number may be chosen from nums an unlimited number of times
# two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different
# you may return the combinations in any order and the order of the numbers in each combination can be in any order

# to avoid duplicate combinations, we will use a DFS algorithm as follows
# the DFS method will have an index (of the nums list) that we have to branch off from (whether we include that element or not)
# if we decide to include it in our list, then we continue to have the option to include more
# if we decide not to include it, then we lose that option and our index gets incremented to the next
# the base cases are as follows:
# if the currSum == target, then we append combination to result and return
# if the index == len(nums), or if the currSum > target, then we return

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(combination.copy())
                return
            if i == len(nums) or currSum > target:
                return
            
            # branch 1: include nums[i], then call dfs(i) since we can choose to include nums[i] again
            combination.append(nums[i])
            dfs(i, currSum + nums[i])

            # branch 2: don't include nums[i], then call dfs(i + 1) since we no longer have the option to include nums[i] ever again
            combination.pop()
            dfs(i + 1, currSum)
        
        dfs(0, 0)

        return res