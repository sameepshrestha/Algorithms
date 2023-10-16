# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        position = [i for i, char in enumerate(s) if char in vowels]
        
        if len(position) <= 1:
            return s   
        start_index = 0 
        returnword = ""
        for i in range(len(position)):
                returnword += s[start_index:position[i]]
                returnword += s[position[len(position)-1-i]]
                start_index = position[i]+1
        returnword += s[position[-1] + 1:]
        return returnword
