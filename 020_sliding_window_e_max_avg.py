## PROBLEM URL: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = sum(nums[0:k])
        max_avg = max_sum / k
        cur_sum = max_sum
        for i in range(1, len(nums)-(k-1)):
            cur_sum = cur_sum - nums[i-1]
            cur_sum = cur_sum + nums[i+(k-1)]
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_avg = max_sum / k
        return max_avg


if __name__ == "__main__":
    nums = [0, 4, 0, 3, 2]
    k = 1
    sol = Solution()
    print(sol.findMaxAverage(nums, k))
