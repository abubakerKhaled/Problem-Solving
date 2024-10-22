## PROBLEM URL: https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        result = 0  # Start with 0 as the maximum area

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            result = max(result, h * w)  # Update result with max area

            # Move the pointer corresponding to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result


if __name__ == "__main__":
    height = [8, 7, 2, 1]
    sol = Solution()
    print(sol.maxArea(height))
