# LeetCode 11: Excel Sheet Column Title
# Level: Easy
class Solution(object):
    def convertToTitle(self, columnNumber):
        str_1 = {"a": 1, "b":2 , "c":3 , "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20,
                 "u": 21, "v":22, "w":23, "x":24, "y":25, "z":26}
        for letter, number in str_1.items():
            if columnNumber == number:
                output = letter

                return output

sol = Solution()
result = sol.convertToTitle(26)
print("Output:", result)

