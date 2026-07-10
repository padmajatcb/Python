#Leet17: Fibonacci Sequence
#level: Easy
class Solution(object):
    def fib(self, n):
        fib_list = [0, 1]

        if n == 0:
            return 0
        if n == 1:
            return fib_list
        for i in range(2, n + 1):
            check1 = fib_list[-1]
            check2 = fib_list[-2]

            next_num = check1 + check2
            fib_list.append(next_num)

        return fib_list


sol = Solution()
result = sol.fib(10)
print("Output:", result)


        # if n == 0:
        #     f_zero = 0
        #     return f_zero
        # if n == 1:
        #     f_one = 1
        #     return f_one
        # if n >= 2:
        #     for i in range(0, n + 1):
        #         x = (i - 1) + (i - 2)
        #         print(f"i = {i} ---- x = {x}")
        #
        #     return x


#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# 2 + 1 = 3
# 3 + 2 = 5
# 5 + 3 = 8
# 8 +
#f(0) = 0,
#f(1) = 1,
# #f(2) = f(1)+ f(0) = 1,
#  #f(3) = f(2) + f(1) = 1 + 1 = 2,
#       f(4) = f(3) + f(2) = 3
#f(5) = f(4) + f(3) = 3 + 2 = 5
