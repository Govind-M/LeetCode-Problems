# class Solution:
#     def coinChange(self, coins: list[int], amount: int) -> int:

#         dp = {}
        
#         def fn(remAmount):

#             if remAmount == 0:
#                 return 0
#             if remAmount < 0:
#                 return -1

#             if remAmount in dp:
#                 return dp[remAmount]
            
#             minCoins = float('inf')

#             for i in range(len(coins)):
#                 res = fn(remAmount - coins[i])

#                 if res != -1 :
#                     minCoins = min(minCoins, 1 + res)
            
#             if minCoins == float('inf'):
#                 dp[remAmount] = -1
#                 return -1
#             else:
#                 dp[remAmount] = minCoins
#                 return minCoins

        
#         return fn(amount)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for remAmount in range(1,amount+1):
            for j in range(len(coins)):
                if remAmount - coins[j] >= 0:
                    dp[remAmount] = min(dp[remAmount], 1 + dp[remAmount-coins[j]])


        print(dp)

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]