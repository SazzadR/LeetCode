# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        number_index_pair = dict()

        for index, number in enumerate(numbers):
            differrence = target - number
            if differrence in number_index_pair:
                return [number_index_pair[differrence], index]
            number_index_pair[number] = index


# numbers = [2, 7, 11, 15]
# target = 18
# solution = Solution()
# response = solution.two_sum(numbers=numbers, target=target)
# print(response)
