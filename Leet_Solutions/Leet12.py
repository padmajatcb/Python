# LeetCode 13: Valid Perfect square
# Level: Easy

import math
class Solution(object):
    def isPerfectSquare(self, num):
        if num!= 0:
            output = int(math.sqrt(num))
            if output * output == num:
                return True
            else:
                return False


sol = Solution()
result = sol.isPerfectSquare(64)
print("Output:", result)


