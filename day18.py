# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

 

# Constraints:

#     1 <= s.length <= 104
#     s contains English letters (upper-case and lower-case), digits, and spaces ' '.
#     There is at least one word in s.

 

# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?


# Use the strip function (or equivalent) to remove unnecessary spaces at the beginning and end of the string.
# Split the string into words: Use the split method to break the string into a list of words. By default, it handles multiple spaces correctly.
# Reverse the list of words: Reverse the order of words using slicing or the reverse method.
# Join the words with a single space: Use the join method to concatenate the reversed words into a single string separated by spaces.

def reverseWords(s: str) -> str:
    # Step 1: Trim leading/trailing spaces and split the string by spaces
    words = s.strip().split()
    # Step 2: Reverse the list of words
    words.reverse()
    # Step 3: Join the reversed words with a single space
    return " ".join(words)

# Example usage
print(reverseWords("the sky is blue"))       # Output: "blue is sky the"
print(reverseWords("  hello world  "))       # Output: "world hello"
print(reverseWords("a good   example"))      # Output: "example good a"
