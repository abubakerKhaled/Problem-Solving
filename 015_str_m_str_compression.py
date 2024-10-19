## PROBLEM URL: https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
import unittest


class Solution:
    def compress(self, chars: list[str]) -> int:
        result = ""
        curr = 0
        count = 0
        next = 1
        while curr < len(chars):
            if next < len(chars) and chars[curr] == chars[next]:
                next += 1
                count += 1
            else:
                count += 1
                result += chars[curr]
                if count > 1:
                    result += str(count)
                count = 0
                curr = next
                next += 1
        for i in range(len(result)):
            chars[i] = result[i]
        return len(result)




class TestStringCompression(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_compression(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected_chars = ["a", "2", "b", "2", "c", "3"]
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 6)
        self.assertEqual(chars[:compressed_length], expected_chars)

    def test_single_characters(self):
        chars = ["a", "b", "c"]
        expected_chars = ["a", "b", "c"]
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 3)
        self.assertEqual(chars[:compressed_length], expected_chars)

    def test_all_same_characters(self):
        chars = ["a", "a", "a", "a"]
        expected_chars = ["a", "4"]
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 2)
        self.assertEqual(chars[:compressed_length], expected_chars)

    def test_two_different_characters(self):
        chars = ["a", "a", "b", "b"]
        expected_chars = ["a", "2", "b", "2"]
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 4)
        self.assertEqual(chars[:compressed_length], expected_chars)

    def test_single_character_repeated(self):
        chars = ["a"]
        expected_chars = ["a"]
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 1)
        self.assertEqual(chars[:compressed_length], expected_chars)

    def test_empty_list(self):
        chars = []
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 0)
        self.assertEqual(chars, [])

    def test_no_compression_needed(self):
        chars = ["a", "b", "c", "d"]
        expected_chars = ["a", "b", "c", "d"]
        compressed_length = self.sol.compress(chars)
        self.assertEqual(compressed_length, 4)
        self.assertEqual(chars[:compressed_length], expected_chars)


if __name__ == "__main__":
    unittest.main()
