# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        elem_index = {}
        for i, elem in enumerate(nums):
            if target - elem in elem_index:
                return [i, elem_index[target - elem]]
            else:
                elem_index[elem] = i


print(Solution().twoSum([2,7,11,15], 9))