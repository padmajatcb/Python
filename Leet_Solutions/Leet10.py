# LeetCode 10: Single Number
# Level: Easy
class Solution(object):
    def singleNumber(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                count += 1
            elif nums.count(nums[i]) == 1:
                output = nums[i]
                return output

sol = Solution()
nums = [4,1,2,1,2]
result = sol.singleNumber(nums)
print("Output:", result)

