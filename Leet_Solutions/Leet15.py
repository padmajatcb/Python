# LeetCode 16: Find Common Characters
# Level: Easy
class Solution(object):
    def commonChars(self, words):
        output = []
        character = ['a', 'b', 'c', 'd', "e", 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(len(words)):
            for j in range(len(character)):
                if character[j] in words[i]:
                    output.append(character[j])



            return output

sol = Solution()
result = sol.commonChars(["bella","label","roller"])
print("Output:", result)




