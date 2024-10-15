## PROBLEM URL: https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        ok = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 1 and n != 0:
            return False

        # if the first element and the second is zero then there is a place to plant
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] += 1
            ok += 1
        for idx in range(1, len(flowerbed) - 1):
            # if the prev and element and next are zero then there is a place to plant
            if (
                flowerbed[idx - 1] == 0
                and flowerbed[idx] == 0
                and flowerbed[idx + 1] == 0
            ):
                flowerbed[idx] += 1
                ok += 1
        if len(flowerbed) > 1:
            # if prev and last elements are zero then there is a place to plant
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                ok += 1
        # check if the places to plant is equal to the plants then return True
        if ok >= n:
            return True
        # else return False
        return False


class TestCanPlaceFlowers(unittest.TestCase):
    def setUp(self):
        self.slo = Solution()

    def test_single_empty_spot(self):
        # Test when flowerbed has only one spot and it's empty, n = 1
        self.assertTrue(self.slo.canPlaceFlowers([0], 1))

    def test_single_occupied_spot(self):
        # Test when flowerbed has only one spot and it's already occupied, n = 1
        self.assertFalse(self.slo.canPlaceFlowers([1], 1))

    def test_single_empty_spot_n_0(self):
        # Test when flowerbed has only one spot, it's empty, and no flowers to place
        self.assertTrue(self.slo.canPlaceFlowers([0], 0))

    def test_single_occupied_spot_n_0(self):
        # Test when flowerbed has only one spot, it's occupied, and no flowers to place
        self.assertTrue(self.slo.canPlaceFlowers([1], 0))

    def test_multiple_empty_spots(self):
        # Test with multiple empty spots
        self.assertTrue(self.slo.canPlaceFlowers([0, 0, 1, 0, 0], 1))

    def test_no_planting_possible(self):
        # Test with no possible planting spots
        self.assertFalse(self.slo.canPlaceFlowers([1, 0, 1, 0, 1], 1))

    def test_planting_possible_edge_case(self):
        # Test where there are enough spots only at the start and end of the flowerbed
        self.assertTrue(self.slo.canPlaceFlowers([0, 0, 1, 0, 0], 2))

    def test_flowerbed_with_alternating_zeros_and_ones(self):
        # Test when the flowerbed alternates between empty and planted
        self.assertFalse(self.slo.canPlaceFlowers([1, 0, 1, 0, 1, 0], 1))

    def test_large_flowerbed(self):
        # Test with a large flowerbed with sufficient space
        self.assertTrue(self.slo.canPlaceFlowers([0, 0, 0, 0, 0, 1, 0, 0, 0], 3))

    def test_exact_fit(self):
        # Test where flowerbed has exactly the number of spaces needed
        self.assertTrue(self.slo.canPlaceFlowers([0, 0, 0], 1))

    def test_plant_more_than_possible(self):
        # Test when trying to plant more flowers than possible
        self.assertFalse(self.slo.canPlaceFlowers([0, 0, 1, 0, 0], 3))

    def test_no_empty_spots(self):
        # Test when flowerbed has no empty spots
        self.assertFalse(self.slo.canPlaceFlowers([1, 1, 1, 1, 1], 1))


if __name__ == "__main__":
    unittest.main()