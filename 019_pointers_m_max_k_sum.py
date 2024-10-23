## PROBLEM URL: https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
import unittest


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        size = len(nums)
        left = 0
        right = size - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                right -= 1
                left += 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return count




class TestMaxOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        nums = [1, 3, 3, 3, 4]
        k = 6
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 1)  # One pairs (3, 3)

    def test_no_pairs(self):
        nums = [1, 2, 3, 4, 5]
        k = 10
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)  # No pairs sum up to 10

    def test_all_same_elements(self):
        nums = [2, 2, 2, 2]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)  # Two pairs (2, 2)

    def test_single_element(self):
        nums = [5]
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)  # No pairs can be formed with a single element

    def test_empty_list(self):
        nums = []
        k = 5
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 0)  # No operations on an empty list

    def test_duplicates_but_not_enough_pairs(self):
        nums = [3, 1, 3, 1, 2]
        k = 4
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)  # Two pairs (3, 1), and (3, 1)

    def test_large_numbers(self):
        nums = [1000000, 1000000, 1000000, 1000000]
        k = 2000000
        result = self.solution.maxOperations(nums, k)
        self.assertEqual(result, 2)  # Two pairs (1000000, 1000000)


if __name__ == "__main__":
    unittest.main()
