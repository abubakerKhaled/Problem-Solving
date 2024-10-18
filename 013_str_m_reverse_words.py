## PROBLEM URL: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # words = words[::-1]
        return " ".join(s.split()[::-1])

if __name__ == "__main__":
    s = 'the sky is blue'
    sol = Solution()
    print(sol.reverseWords(s))
