#Leet-code problem 1
#Remove duplicates from sorted array
#Input: nums = [1,1,2]
#Output: 2, nums = [1,2,_]
#Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).

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


#Unique_elements = k
#traverse through the array
#Does any number appear more than once? If yes, replace that number with an underscore
#If not, keep the order and return k