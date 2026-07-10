# #LeetCode 7: Sort Colors #Come back tomorrow - Tuesday, June 23
# #Level: Medium
#
# #Tuesday, June 23: With the help of gemini and by understanding it I have solved the below
# class Solution(object):
#     def sortColors(self, nums):
#         low = 0 #Low is the start of the very first index
#         mid = 0 #Starts at the index and scans
#         high =  len(nums) - 1 #points to the highest element in the array
#
#         while mid <= high:
#             if nums[mid] == 0:
#                 nums[mid], nums[low] = nums[low], nums[mid]
#                 low += 1
#                 mid += 1
#
#             elif nums[mid] == 1:
#                 mid += 1
#
#             elif nums[mid] == 2:
#                 nums[mid], nums[high] = nums[high], nums[mid]
#                 high -= 1
#Confused, coming back to this


# sol = Solution()
# nums = []
# sol.sortColors(nums)
# print("Output:", nums)

