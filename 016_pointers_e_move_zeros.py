## PROBLEM URL: https://leetcode.com/problems/move-zeroes/?source=submission-ac
import unittest


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size <= 1 or 0 not in nums:
            return
        ele = [0] * size
        first = 0
        last = size - 1
        idx = size - 1
        while first < size:
            ele[idx] = nums[idx]
            if nums[first] == 0:
                nums[last] = 0
                last -= 1
            first += 1
            idx -= 1
        first = 0
        for i in range(len(ele)):
            if ele[i] != 0:
                nums[first] = ele[i]
                first += 1
        del ele



class TestMoveZeroes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        nums = [1]
        expected = [1]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

        nums = [0]
        expected = [0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_all_non_zero_elements(self):
        nums = [1, 2, 3, 4]
        expected = [1, 2, 3, 4]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_all_zero_elements(self):
        nums = [0, 0, 0]
        expected = [0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_mixed_zero_and_non_zero(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_no_zeroes(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_multiple_zeroes(self):
        nums = [0, 0, 1, 0, 2, 0, 3]
        expected = [1, 2, 3, 0, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_zeroes_at_the_end(self):
        nums = [1, 2, 3, 0, 0, 0]
        expected = [1, 2, 3, 0, 0, 0]
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_empty_list(self):
        nums = []
        expected = []
        self.solution.moveZeroes(nums)
        self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
