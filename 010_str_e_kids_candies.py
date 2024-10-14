## PROBLEM URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
import unittest


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        def is_greatest(candies: list[int], extra_candy: int, kid: int) -> bool:
            candies_copy = candies[:]
            candy = candies_copy[kid] + extra_candy
            candies_copy[kid] = candy
            max_candy = candy
            for kid_candy in candies:
                if kid_candy > max_candy:
                    max_candy = kid_candy
            if candy == max_candy:
                return True
            return False

        resests = []
        for kid in range(len(candies)):
            resests.append(is_greatest(candies, extraCandies, kid))
        return resests


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_all_kids_can_have_greatest_candies(self):
        # All kids will have the greatest number of candies
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        expected = [True, True, True, False, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_some_kids_can_have_greatest_candies(self):
        # Some kids will have the greatest number of candies
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        expected = [True, False, False, False, False]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_single_kid(self):
        # Test with only one kid
        candies = [5]
        extraCandies = 3
        expected = [True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_all_candies_same(self):
        # All kids have the same number of candies
        candies = [5, 5, 5, 5]
        extraCandies = 2
        expected = [True, True, True, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_no_extra_candies(self):
        # No extra candies are given
        candies = [1, 2, 3, 4]
        extraCandies = 0
        expected = [False, False, False, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)


if __name__ == "__main__":
    unittest.main()
