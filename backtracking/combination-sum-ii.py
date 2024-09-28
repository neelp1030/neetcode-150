# you are given an array of integers candidates, which may contain duplicates, and a target integer target
# your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target
# each element from candidates may be chosen at most once within a combination
# the solution set must not contain duplicate combinations
# you may return the combinations in any order and the order of the numbers in each combination can be in any order

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        candidates.sort()

        def dfs(i, currSum):
            if currSum == target:
                res.append(combination.copy())
                return
            
            if i == len(candidates) or currSum > target:
                return
            
            # branch 1: include nums[i], then call dfs(i + 1) since we can choose to include more of the same value
            combination.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])

            # branch 2: don't include nums[i], then increment i until nums[i] != nums[i + 1], then call dfs(i + 1), since we no longer have the option to include nums[i] ever again
            combination.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, currSum)
        
        dfs(0, 0)

        return res