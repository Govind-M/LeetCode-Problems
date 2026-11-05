class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        
        dp = {}

        def fn(n):
            
            if n<=1:
                return 0

            if n in dp:
                return dp[n]

            dp[n] = min(fn(n-1)+cost[n-1],fn(n-2)+cost[n-2])
            return dp[n]

        return fn(len(cost))