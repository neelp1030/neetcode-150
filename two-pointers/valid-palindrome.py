# given a string s, return true if it is a palindrome, otherwise return false
# a palindrome is a string that reads the same forward and backward
# it is also case-insensitive and ignores all non-alphanumeric characters

# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:
# Input: s = "tab a cat"
# Output: false
# Explanation: "tabacat" is not a palindrome.

# we will need a helper function to check if a given character is alphanumeric or not, never mind, python has a built-in isalnum() method
# as for the actual algorithm, we can use two pointers l and r that are initialized to the start and end of the string s respectively
# at every step of the process, we will check to make sure the characters at l and r are the same and then move both pointers inwards
# if we ever encounter a non-alphanumeric character on l and/or r, we will move the pointer further inwards
# our stop condition will be either if at any given point the characters at l and r are not equal, or until the l pointer goes past the r pointer (since at that point we are doing redundant verification)
# we also need to make sure we are converting to lowercase (to make it case-insensitive) before comparing using .lower()

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1 
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        
        return True

# time complexity: O(n)
# space complexity: O(1)