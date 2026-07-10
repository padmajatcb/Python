#LeetCode 6: Sqrt(x) (Used a gemini to help me on some concepts, but solved it!)
#Level: Easy
import math


class Solution(object):
    def mySqrt(self, x):
        result = math.sqrt(x)
        return int(result)


sol = Solution()
res = sol.mySqrt(2.5)
print("Output:", res)