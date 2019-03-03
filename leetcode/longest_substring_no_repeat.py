# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# SLIDING Window O(n)
#
# String: abcadcef
# start:  ^
# end:       ^
#
# seen:{
#     a:0,
#     b:1,
#
# }
#
# max_length: 4
#
# Algorithm:
# - Start with start and end at 1st char
# - Move end and insert the elem and index in dict seen (Also increment max Lenght) as long as the inserted char is not already in the dict
# - If inserted char is in the dict, move start to position +1 from its last location
# - End of string


def longest_substring_without_repeat(string):
    seen = {}
    max_length = 0
    start = 0
    # move the end
    for end in range(len(string)):
        # if char is in seen, move the start
        if string[end] in seen:
            start = max(start, seen[string[end]] + 1)
        # Insert in seen
        seen[string[end]] = end
        # max_len is max of existing or end-start + 1
        max_length = max(max_length, end-start + 1)
    return max_length


