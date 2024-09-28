# given a string s, split s into substrings where every substring is a palindrome
# return all possible lists of palindromic substrings
# you may return the solution in any order

# dfs(i), i represents the start of the substring we have left to partition

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(i):
            if i == len(s):
                res.append(partition.copy())
                return

            for j in range(i, len(s)):
                if isPali(s, i, j):
                    partition.append(s[i : j + 1])
                    dfs(j + 1)
                    partition.pop()
            
        dfs(0)

        return res