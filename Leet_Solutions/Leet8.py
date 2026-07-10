# LeetCode 9: Merge Sorted Array
# Level: Easy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Replace the last 'n' elements (the zeros) with nums2
        nums1[m:] = nums2

        # Sort the entire array in-place
        nums1.sort()


runner = Solution()
test_nums1 = [1, 2, 3, 0, 0, 0]
test_m = 3
test_nums2 = [2, 5, 6]
test_n = 3
runner.merge(test_nums1, test_m, test_nums2, test_n)


#nums1 and nums2 are sorted in an non-decreasing order
#n and m represents the num of elements in nums1 and nums2
#Task: Merge nums1 and nums2 into a single array sorted in non-decreasing order
#You cannot create a new array