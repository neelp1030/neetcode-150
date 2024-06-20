# design an algorithm to encode a list of strings to a single string
# the encoded string is then decoded back to the original list of strings
# please implement encode and decode

# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

# before each word, we will need to provide some metadata information to help us decode the string
# for instance, example 1 can be turned into 4@neet4@code4@love3@you
# during the encoding process, for each word we get its length and then add a separator after it (single character, here we choose @)
# during the decoding process, we see 4, so we know after the @ that follows, the next 4 letters are the word, and then it repeats
# even if we have numbers and @ in our words themselves, this will work, as we have encoded in a manner that will not be ruined by these things

class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for s in strs:
            encodedStr += f"{len(s)}@{s}"
        
        return encodedStr

    def decode(self, s: str) -> List[str]:
        index = 0
        res = []

        while index < len(s):
            startOfLenIndex = index

            while s[index] != '@':
                index += 1
            
            lengthOfWord = int(s[startOfLenIndex:index])

            index += 1
            
            res.append(s[index:index + lengthOfWord])

            index += lengthOfWord
        
        return res

# time complexity: O(n)
# space complexity: O(1)