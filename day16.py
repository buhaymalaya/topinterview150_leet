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

# def strStr(haystack: str, needle: str) -> int:
#     return haystack.find(needle)

# # Example 1
# haystack = "sadbutsad"
# needle = "sad"
# print(strStr(haystack, needle))  # Output: 0

# # Example 2
# haystack = "leetcode"
# needle = "leeto"
# print(strStr(haystack, needle))  # Output: -1



def strStr(haystack: str, needle: str) -> int:
    # Get the lengths of haystack and needle
    haystack_len = len(haystack)
    needle_len = len(needle)

    # If the needle is longer than the haystack, it can't be found
    if needle_len > haystack_len:
        return -1

    # Iterate through the haystack, checking each substring of the same length as the needle
    for i in range(haystack_len - needle_len + 1):
        # Check if the substring matches the needle
        if haystack[i:i + needle_len] == needle:
            return i