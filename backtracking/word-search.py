# given a 2D grid of characters board and a string word, return true if the word is present in the grid, otherwise return false
# for the word to be present, it must be possible to form it with a path in the board with horizontally or vertically neighbouring cells
# the same cell may not be used more than once in a word

# we can try running dfs starting from each cell in the grid
# the dfs function will be dfs(i), where i refers to the index in the word up until which we have matched so far
# visiting set will track cells in the current path being considered
# base cases for the dfs function are as follows
# if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visiting, then we return False
# if i == len(word), then we have successfully matched the full word, so we return True
# if board[r][c] == word[i], then we have successfully matched the current letter, so we return the OR of DFS calls on all neighbouring cells

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visiting = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visiting or board[r][c] != word[i]:
                return False
            
            visiting.add((r, c))

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            visiting.remove((r, c))
                    
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False