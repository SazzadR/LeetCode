# https://leetcode.com/problems/find-pivot-index/
from typing import List


class Solution:
    def pivot_index(self, numbers: List[int]) -> int:
        for index, number in enumerate(numbers):
            left_side = numbers[0:index]
            right_side = numbers[index + 1 :]

            sum_of_left_side = sum(left_side)
            sum_of_right_side = sum(right_side)
            if sum_of_left_side == sum_of_right_side:
                return index

        return -1


# numbers = [1, 7, 3, 6, 5, 6]
# solution = Solution()
# response = solution.pivot_index(numbers)
# print(response)
