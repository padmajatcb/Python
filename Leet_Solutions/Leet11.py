# LeetCode 12: Self dividing numbers
# Level: Easy
# Both left and right cannot have zero in their digits
# Left from right should be perfectly divisible
# If a number doesn't divide properly even though it doesn't have 0 in it, it's invalid
# Left and right has to be inclusive

class Solution(object):
    def selfDividingNumbers(self, left, right):
        result_list = []

        for lis_num in range(left, right + 1):

            is_self_dividing = True

            for digit_str in str(lis_num):
                digit = int(digit_str)

                if digit == 0 or lis_num % digit != 0:
                    is_self_dividing = False
                    break

            if is_self_dividing:
                result_list.append(lis_num)

        return result_list

sol = Solution()
result = sol.selfDividingNumbers(1, 22)
print("Output:", result)
