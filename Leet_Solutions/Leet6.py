#LeetCode 6: Sqrt(x) 
#Level: Easy
import math


class Solution(object):
    def mySqrt(self, x):
        result = math.sqrt(x)
        return int(result)


sol = Solution()
res = sol.mySqrt(2.5)
print("Output:", res)
