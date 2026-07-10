# Longest Palindromic substance: Problem #3
# class Solution(object):
#     def longestPalindrome(self, s):
#         count = 0
#         output = ""
#         for i in range(len(s)):
#             if s != " ":
#             if s == s[::-1]:
#                 return s
#             else:
#                 return False


# sol = Solution()
# input_string = "babad"
# result = sol.longestPalindrome(input_string)
# print("Output:", result)

# def is_palindrome(string):
#     alnum_string = ''.join(char for char in string if char.isalnum()).lower()  # Clean and lower case
#     return alnum_string == alnum_string[::-1]  # Compare cleaned string with its reverse
#
# # Test the function
# word = input("Please enter a word or sentence to check: ")
# if is_palindrome(word):
#     print(f"'{word}' is a palindrome.")
# else:
#     print(f"'{word}' is not a palindrome.")
