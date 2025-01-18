# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters.

def longest_common_prefix(strs):
    # If the input list is empty, return an empty string
    if not strs:
        return ""
    
    # Find the shortest string in the array, as the common prefix cannot
    # be longer than the shortest string
    shortest = min(strs, key=len)

    # Initialize the prefix to the shortest string
    for i in range(len(shortest)):
        # Compare the characters of the shortest string with the others
        for string in strs:
            if string[i] != shortest[i]:
                # If a mismatch is found, return the prefix up to that point
                return shortest[:i]
            
     # If no mismatch is found, the entire shortest string is the prefix
    return shortest

# Example usage:
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]

print(longest_common_prefix(strs1))  # Output: "fl"
print(longest_common_prefix(strs2))  # Output: ""