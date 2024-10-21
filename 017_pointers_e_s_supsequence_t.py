## PROBLEM URL: https://leetcode.com/problems/is-subsequence/?source=submission-ac


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        size = len(t)
        s_pointer = 0
        t_pointer = 0
        while t_pointer < size:
            if s_pointer == len(s):
                return True
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1

        if s_pointer == len(s):
            return True
        return False


def test_is_subsequence():
    sol = Solution()

    # Test case 1: s is a subsequence of t
    s = "abc"
    t = "ahbgdc"
    assert sol.isSubsequence(s, t) == True, "Test case 1 failed"

    # Test case 2: s is not a subsequence of t
    s = "axc"
    t = "ahbgdc"
    assert sol.isSubsequence(s, t) == False, "Test case 2 failed"

    # Test case 3: s is empty, should return True
    s = ""
    t = "ahbgdc"
    assert sol.isSubsequence(s, t) == True, "Test case 3 failed"

    # Test case 4: t is empty but s is not, should return False
    s = "abc"
    t = ""
    assert sol.isSubsequence(s, t) == False, "Test case 4 failed"

    # Test case 5: s and t are both empty, should return True
    s = ""
    t = ""
    assert sol.isSubsequence(s, t) == True, "Test case 5 failed"

    # Test case 6: s is longer than t, should return False
    s = "abcdef"
    t = "abc"
    assert sol.isSubsequence(s, t) == False, "Test case 6 failed"

    # Test case 7: s contains only one character, present in t
    s = "a"
    t = "ahbgdc"
    assert sol.isSubsequence(s, t) == True, "Test case 7 failed"

    # Test case 8: s contains only one character, not present in t
    s = "z"
    t = "ahbgdc"
    assert sol.isSubsequence(s, t) == False, "Test case 8 failed"

    # Test case 9: All characters of s are in t, but in the wrong order
    s = "cba"
    t = "abc"
    assert sol.isSubsequence(s, t) == False, "Test case 9 failed"

    # Test case 10: s contains repeated characters, and t has enough matching sequence
    s = "aaa"
    t = "aabbbaa"
    assert sol.isSubsequence(s, t) == True, "Test case 10 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_is_subsequence()
