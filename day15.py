# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

#     A word is defined as a character sequence consisting of non-space characters only.
#     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#     The input array words contains at least one word.

 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

 

# Constraints:

#     1 <= words.length <= 300
#     1 <= words[i].length <= 20
#     words[i] consists of only English letters and symbols.
#     1 <= maxWidth <= 100
#     words[i].length <= maxWidth


def fullJustify(words, maxWidth):
    result = []  # Stores the final list of justified lines
    line = []  # Stores the current line's words
    line_length = 0

    for word in words:
        # Check if adding this word would exceed maxWidth
        if line_length + len(word) + len(line) > maxWidth:
            # Distribute spaces for the current line

            for i in range(maxWidth - line_length):
                # Distribute extra spaces from left to right
                line[i % (len(line) - 1 or 1)] += " "

            # Add the justified line to result
            result.append("".join(line))
            # Reset for the next line
            line, line_length = [], 0

        # Add the current word to the line
        line.append(word)
        line_length += len(word)

    # Handle the last line: Left-justified with spaces at the end
    result.append(" ".join(line).ljust(maxWidth))
    return result