# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List


# 双指针解法：遍历这个有序数组
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenght = len(nums)
        if lenght <= 1:
            return lenght

        left = 0
        for right in range(1, lenght):
            if nums[left] != nums[right]:
                left += 1
                if left < right:
                    nums[left] = nums[right]
        return left + 1
