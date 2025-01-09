# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

# Constraints:

#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# Example 1
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))  # Output: 0

# Example 2
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))  # Output: -1