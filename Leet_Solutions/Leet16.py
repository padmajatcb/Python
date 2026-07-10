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

