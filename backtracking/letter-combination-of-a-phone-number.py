# you are given a string digits made up of digits from 2 through 9 inclusive
# each digit (not including 1) is mapped to a set of characters as shown below:
# a digit could represent any one of the characters it maps to
# return all possible letter combinations that digits could represent
# you may return the answer in any order

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToLetterMap = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }

        def dfs(i, combination):
            if i == len(digits):
                res.append(combination)
                return
            
            for letter in digitToLetterMap[digits[i]]:
                dfs(i + 1, combination + letter)
            
        if not digits:
            return []
        
        dfs(0, "")

        return res