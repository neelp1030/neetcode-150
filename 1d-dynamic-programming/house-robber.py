# you are given an integer array nums where nums[i] represents the amount of money the ith house has
# the houses are arranged in a straight line, i.e. the ith house is the neighbour of the (i - 1)th and (i + 1)th house
# you are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into
# return the maximum amount of money you can rob without alerting the police

# let's think of the problem in terms of a decision tree
# first we have to decide whether or not to rob the very first house
# if we rob it, then we have to skip the house right after it, so the new subproblem will start on the second house after it
# if we do not rob it, then our new subproblem will start on the house right after it
# after drawing out the decision tree, we see that there are a lot of repeated subproblems, so we can use a dynamic programming approach
# let's try to do bottom-up approach
# let n represent len(nums)
# f(n) means we don't have any houses left to rob anymore, so f(n) = 0
# f(n - 1) means we have just the last house left to rob, so f(n - 1) = nums[n - 1]
# then we can work our way backwards towards f(0), which will be the result
# how do we determine f(x)? well we can either rob house x or not
# if we rob house x, then f(x) = nums[x] + f(x + 2), since we have to skip house (x + 1)
# if we don't rob house x, then f(x) = f(x + 1), since we no longer have to skip house (x + 1)
# thus, f(x) = max(nums[x] + f(x + 2), f(x + 1)), and we work our way backwards towards f(0)
# we can see that each f(x) only depends on f(x + 2) and f(x + 1), so we will only need constant space if we do it efficiently
# we will be computing f(n - 2) through f(0)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = nums[n - 1]
        n2 = 0

        for i in range(n - 2, -1, -1):
            temp = max(nums[i] + n2, n1)
            n2 = n1
            n1 = temp
        
        return n1