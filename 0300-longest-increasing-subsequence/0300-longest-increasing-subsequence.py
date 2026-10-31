class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:

        dp = [1] * len(nums)
        lisLength = dp[0]
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    lisLength = max(lisLength,dp[i])
        
        return lisLength

