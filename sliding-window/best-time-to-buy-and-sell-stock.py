# you are given an integer array prices where prices[i] is the price of NeetCoin on the ith day
# you may choose a single day to buy one NeetCoin and choose a different day in the future to sell it
# return the maximum profit you can achieve
# you may choose to not make any transactions, in which case the profit would be 0

# Example 1:
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:
# Input: prices = [10,8,7,5,2]
# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# we can use a sliding window technique, where we initialize our l ptr and r ptr to 1st and 2nd day respectively
# the l ptr is our buying price, and the r ptr is our selling price
# if our selling price is lower than our buying price, then there's no reason to consider it, so we set l ptr to r ptr and increment r ptr
# otherwise, we can keep expanding our sliding window (incrementing just the r ptr)
# loop condition will always be based on r ptr within bounds

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxProfit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            r += 1
        
        return maxProfit

# time complexity: O(n)
# space complexity: O(1)