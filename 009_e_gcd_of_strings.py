## PROBLEM URL: https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        :type str1:str
        :type str2:str
        :rtype: str
        """
        if (str1 + str2 != str2 + str1):
            return "None"

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        return str1[:gcd(len(str1), len(str2))]

if __name__ == "__main__":
    sol = Solution()
    tests = [["ABAB", "ABABABABAB"], ["ABCABC", "ABC"], ["LEET", "CODE"]]
    for test in tests:
        print(f'TEST: {test[0]}, {test[1]} -> {sol.gcdOfStrings(test[0], test[1])}')
