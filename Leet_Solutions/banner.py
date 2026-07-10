#leet code problem 2
#Medium: Longest substring without repeating characters
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         if s == '':
#             return 0
#
#         new_string = ''
#         count = 0
#         for i in range(len(s)):
#             tracker = s[i]
#             new_string = tracker + new_string
#             count += 1
#         if new_string.count(tracker) > 1:
#             while new_string.count(tracker) > 1:
#                 new_string = new_string[::-1]
#         if len(new_string) > count:
#             count = len(new_string)
#             return new_string

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0

        new_string = ''
        max_count = 0

        for i in range(len(s)):
            tracker = s[i]

            new_string = tracker + new_string


            if new_string.count(tracker) > 1:
                while new_string.count(tracker) > 1:

                    new_string = new_string[:-1]

            if len(new_string) > max_count:
                max_count = len(new_string)

        return max_count

#Strings are immutable

sol = Solution()
input_string = "pwwkew"
result = sol.lengthOfLongestSubstring(input_string)
print("Output:", result)





