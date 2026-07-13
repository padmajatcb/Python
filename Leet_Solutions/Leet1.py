class Solution(object):
    def removeDuplicates(self, nums):
        new_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] not in new_list:
                new_list = new_list + [nums[i]]

        for i in range(len(new_list)):
            nums[i] = new_list[i]

        k = len(new_list)
        return k


sol = Solution()
test_nums = [1, 1, 2]
result = sol.removeDuplicates(test_nums)
print(result)
