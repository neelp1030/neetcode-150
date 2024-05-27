# given a string s, find the length of the longest substring without duplicate characters
# a substring is a contiguous sequence of characters within a string

# Example 1:
# Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:
# Input: s = "xxxx"
# Output: 1

# since we need to find the longest substring satisfying some condition, it makes sense to use a sliding window technique traversing through the string
# for the sliding window, we will need to keep track of some information to efficiently determine if we have added a duplicate character
# the best way to do this is to use a set to track characters in the sliding window
# whenever we encounter a character that already exists in our set, we start removing characters from the left side of our sliding window until that new character no longer exists in our set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        maxWindowSize = 0

        windowChars = set()

        while r < len(s):
            while s[r] in windowChars:
                windowChars.remove(s[l])
                l += 1

            windowChars.add(s[r])
            maxWindowSize = max(maxWindowSize, r - l + 1)
            r += 1
        
        return maxWindowSize
        
# time complexity: O(n)
# space complexity: O(n)