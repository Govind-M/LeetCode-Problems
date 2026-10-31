class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = {}
        
        def fn(remAmount):

            if remAmount == 0:
                return 0
            if remAmount < 0:
                return -1

            if remAmount in dp:
                return dp[remAmount]
            
            minCoins = float('inf')

            for i in range(len(coins)):
                res = fn(remAmount - coins[i])

                if res != -1 :
                    minCoins = min(minCoins, 1 + res)
            
            if minCoins == float('inf'):
                dp[remAmount] = -1
                return -1
            else:
                dp[remAmount] = minCoins
                return minCoins

        
        return fn(amount)