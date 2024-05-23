# given an array of strings strs, group all anagrams together into sublists.
# you may return the output in any order
# an anagram is a string that contains the exact same characters as another string, but the order of the characters can be different
# strs[i] is made up of lowercase english letters

# example 1
# input: strs = ["act","pots","tops","cat","stop","hat"]
# output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# example 2
# input: strs = ["x"]
# output: [["x"]]

# example 3
# input: strs = [""]
# output: [[""]]

# in order to do this, we can use a hashmap where the key will be a canonical form for all anagrams, and the value will be a list of all the strings that are anagrams
# how to define the canonical form? one way to do it could be a sorted version of the string, but this is inefficient. instead, let's make the canonical form a fixed size (26) array of character frequency
# since the key for a hashmap can't be an array, we can make it a tuple (just convert the array to a tuple)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = collections.defaultdict(list)

        for s in strs:
            charFreq = [0] * 26
            for c in s:
                charFreq[ord(c) - ord('a')] += 1
            
            anagramGroups[tuple(charFreq)].append(s)
        
        return anagramGroups.values()

# time complexity: O(n * m), where n is the number of strings and m is the average length of a string
# space complexity: O(n), worst case, we can have n anagram groups, and the charFreq arrays are all fixed size so that doesn't matter