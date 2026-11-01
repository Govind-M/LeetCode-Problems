class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        n = len(nums)

        dp = [[None] * (target + 1) for _ in range(n)]

        def fn(remSum, start):

            if remSum == 0:
                return True

            if remSum < 0 or start == n:
                return False

            if dp[start][remSum] is not None:
                return dp[start][remSum]

            
            pick = fn(remSum - nums[start], start + 1)

            
            not_pick = fn(remSum, start + 1)

            dp[start][remSum] = pick or not_pick

            return dp[start][remSum]

        return fn(target, 0)