#LeetCode 4: Multiply Strings
#Level: Medium
class Solution(object):
    def multiply(self, num1, num2):
        if num1 and num2 != " ":
            result = int(num1) * int(num2)
            return str(result)

sol = Solution()
res = sol.multiply(123, 456)
print("Output:", res)

