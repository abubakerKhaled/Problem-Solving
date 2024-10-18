## PROBLEM URL: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75


# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         products = []
#         for i in range(len(nums)):
#             sum = 1
#             for j in range(len(nums)):
#                 if j != i:
#                     sum *= nums[j]
#             products.append(sum)
#         return products


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        results = [1] * n
        # calculate the prefix
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # calculate the postfix
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # calculate the products
        for i in range(n):
            results[i] = prefix[i] * postfix[i]

        return results


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.productExceptSelf(nums))
