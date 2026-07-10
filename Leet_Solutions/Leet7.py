# LeetCode 8: Majority element - With the help of gemini, but I understood it!
# Level: Easy
#Took a while to do this since there was one error showing up presistently
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

# The min number of times an element
# must appear to be considered the majority choice

# len(nums) - Counts total num of items in list
# /2 - Splits that total exactly in half

# The problem states that a majority element must appear more than
# [n / 2] times. Therefore, the threshold acts like a finish line.
# As you count how many times a number shows up, you compare it
# to this threshold to see if it won.
