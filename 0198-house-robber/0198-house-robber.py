class Solution:
    def rob(self, nums: list[int]) -> int:
        
        dp = {}

        def fn(n):

            if n == 0:
                return nums[0]

            if n == 1:
                return max(nums[0],nums[1])

            if n in dp:
                return dp[n]

            dp[n] = max(fn(n-2)+nums[n], fn(n-1))

            return dp[n]

        return fn(len(nums)-1)