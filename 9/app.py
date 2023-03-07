# https://leetcode.com/problems/palindrome-number/
class Solution:
    def is_palindrome(self, number: int) -> bool:
        number = str(number)
        length = len(number)

        half_length = length / 2

        response = True

        for index, char in enumerate(number):
            if index + 1 <= half_length:
                if char != number[length - 1 - index]:
                    response = response and False
                    break

        return response


# number = 11211
# solution = Solution()
# solution.is_palindrome(number=number)
