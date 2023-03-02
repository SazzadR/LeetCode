# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List


class Solution:
    def running_sum(self, numbers: List[int]) -> List[int]:
        response = []
        for index, number in enumerate(numbers):
            if len(response):
                response.append(number + response[index - 1])
            else:
                response.append(number)

        return response


# solution = Solution()
# numbers = [3,1,2,10,1]
# response = solution.running_sum(numbers)
# print(response)
