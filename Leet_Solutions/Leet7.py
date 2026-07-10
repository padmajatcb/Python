# LeetCode 8: Majority element 
# Level: Easy

class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        threshold = len(nums) / 2
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > threshold:
                return num

sol = Solution()
nums = [2,2,1,1,1,2,2]
result = sol.majorityElement(nums)
print("Output:", result)

