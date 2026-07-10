# LeetCode 15: Is Subsequence
# Level: Easy
class Solution(object):
    def isSubsequence(self, s, t):
        count_one = 0
        count_two = 0
        while count_one < len(s) and count_two < len(t):
            if s[count_one] == t[count_two]:
               count_one+=1

            count_two += 1

        return count_one == len(s)

sol = Solution()
result = sol.isSubsequence("axc", "ahbgdc")
print("Output:", result)