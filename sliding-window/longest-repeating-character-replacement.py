# you are given a string s consisting of only uppercase english characters and an integer k
# you can choose up to k characters of the string and replace them with any other uppercase english character
# after performing at most k replacements, return the length of the longest substring which contains only one distinct character

# Example 1:
# Input: s = "XYYX", k = 2
# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:
# Input: s = "AAABABB", k = 1
# Output: 5

# once again, we are trying to find the longest substring satisfying some condition, so it makes sense to use a sliding window technique
# how do we check the satisfaction of this condition though?
# we can track the character frequencies of the current window using a hashmap
# each time we update the hashmap (increment a frequency), we can potentially update our max frequency
# when our window and max frequency surpasses the k replacements we are allowed, we condense our window from the left
# but we don't need to bother decrementing the max frequency in this case, since we are looking for the largest window
# a lower max frequency solution will always have a lower window size, so we can ignore those cases without sacrificing correctness

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        
        count = {}

        maxf = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)

# time complexity: O(n)
# space complexity: O(n)