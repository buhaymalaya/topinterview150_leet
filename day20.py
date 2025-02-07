# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of only English letters and spaces ' '.
#     There will be at least one word in s.

def length_of_last_word(s: str) -> int:
    # Strip any trailing spaces and split the string into words
    words = s.strip().split()
    # Return the length of the last word
    return len(words[-1])

s1 = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"

print(length_of_last_word(s1))  # Output: 5
print(length_of_last_word(s2))  # Output: 4
print(length_of_last_word(s3))  # Output: 6

def length_of_last_word(s: str) -> int:
    length = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count the characters of the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length

s1 = "Hello World"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"

print(length_of_last_word(s1))  # Output: 5
print(length_of_last_word(s2))  # Output: 4
print(length_of_last_word(s3))  # Output: 6