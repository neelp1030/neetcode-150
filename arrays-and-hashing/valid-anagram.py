# given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# an anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# s and t consist of lowercase English letters, so we can use a fixed size array instead of a hashmap to store the character frequencies

# example 1
# input: s = "racecar", t = "carrace"
# output: true

# example 2
# input: s = "jar", t = "jam"
# output: false

# we can populate the frequency (increment) of each character of string s through one-pass using a hashmap
# then, we can populate the frequency (decrement) of each character of string t through one-pass using the same hashmap
# if strings s and t are in fact anagrams, then all values in the hashmap must be zero!
# also observe that if len(s) != len(t), then there's no possible way that they can be anagrams of each other, so we can check this at the start

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        charFrequency = [0] * 26

        for i in range(len(s)):
            charFrequency[ord(s[i]) - ord('a')] += 1
            charFrequency[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if charFrequency[i] != 0:
                return False
        
        return True

# time complexity: O(n)
# space complexity: O(1) since array is fixed size!