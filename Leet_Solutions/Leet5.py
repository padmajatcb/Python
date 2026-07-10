#LeetCode 5: Pow(x,n)
#Level: Medium
import math
class Solution(object):
    def myPow(self, x, n):
        result = math.pow(x, n)
        return float(result)

sol = Solution()
res = sol.myPow(2.00000, 10)
print("Output:", res)
