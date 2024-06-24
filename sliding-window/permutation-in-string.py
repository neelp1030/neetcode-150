# you are given two strings s1 and s2
# return true if s2 contains a permutation of s1, or false otherwise
# that means if a permutation of s1 exists as a substring of s2, then return true
# both strings only contain lowercase letters

# Example 1:
# Input: s1 = "abc", s2 = "lecabee"
# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:
# Input: s1 = "abc", s2 = "lecaabee"
# Output: false

# we wish to check if any substring of s2 (continuous!) is a permutation of s1
# there's two parts to this problem
# firstly, we will use the sliding window technique to traverse all valid substrings of s2 and test them out given our condition
# the condition we are looking for is that the substring (defined by the sliding window on s2 at any given point in time) is a permutation of s1
# to track and test whether the current sliding window is a permutation of s1 efficiently, we basically need to ensure that the frequencies of characters in the sliding window and s1 match
# we can track a frequency difference array, since the strings only contain lowercase letters, the array can be fixed size (26)
# it will be initialized to the character frequencies of s1
# as we add/remove characters to/from our sliding window, we will decrement the appropriate character frequencies in the array
# we will also track the number of character frequency matches (difference = 0) at any given time, and update this whenever we add/remove characters in our sliding window
# this way, we won't have to check through the character frequency array every time we modify our sliding window to check if it became a permutation
# if matches = 26, then we will know that the current sliding window is a permutation
# edge case: if s1's length is larger than s2, then under no circumstances can s2 contain a permutation of s1
# we will initialize the sliding window in s2 to be the first s1.length characters of s2, since the underlying requirement for something to be a permutation is being the same length

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_freq_diff = [0] * 26

        for i in range(len(s1)):
            char_freq_diff[ord(s1[i]) - ord('a')] += 1
            char_freq_diff[ord(s2[i]) - ord('a')] -= 1
        
        matches = 0

        for i in range(26):
            if char_freq_diff[i] == 0:
                matches += 1
        
        l = 0
        r = len(s1)

        while r < len(s2):
            if matches == 26:
                return True
            
            char_to_add_index = ord(s2[r]) - ord('a')
            char_freq_diff[char_to_add_index] -= 1

            if char_freq_diff[char_to_add_index] == 0:
                matches += 1
            elif char_freq_diff[char_to_add_index] == -1:
                matches -= 1
            
            char_to_remove_index = ord(s2[l]) - ord('a')
            char_freq_diff[char_to_remove_index] += 1

            if char_freq_diff[char_to_remove_index] == 0:
                matches += 1
            elif char_freq_diff[char_to_remove_index] == 1:
                matches -= 1
            
            l += 1
            r += 1
        
        return matches == 26

# time complexity: O(n)
# space complexity: O(1)