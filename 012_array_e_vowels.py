## PROBLEM URL: https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
import unittest


class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ["a", "e", "i", "o", "u", 'A', 'E', 'I', 'O', 'U']
        letters = []
        positions = []
        final_word = []
        for i in range(len(s)):
            if s[i] in VOWELS:
                letters.append(s[i])
                positions.append(i)
            final_word.append(s[i])
        # reverse the letters
        letters = letters[::-1]
        i = 0
        for pos in positions:
            final_word[pos] = letters[i]
            i += 1
        return "".join(final_word)


if __name__ == "__main__":
    s = "IceCreAm"
    sol = Solution()
    print(sol.reverseVowels(s))