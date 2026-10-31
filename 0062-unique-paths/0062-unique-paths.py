# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = {}

#         def fn(row,col):
            
#             if row == 0 and col == 0:
#                 return 1
            
#             if row < 0 or col < 0:
#                 return 0

#             if (row,col) in dp:
#                 return dp[(row,col)]
            
#             up = fn(row-1, col)
#             left = fn(row, col-1)
#             dp[(row,col)] = up + left

#             return up + left

#         return fn(m-1, n-1)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):

                if row == 0 and col == 0:
                    dp[row][col] = 1
                else:
                    up = dp[row-1][col] if row > 0 else 0
                    left = dp[row][col-1] if col > 0 else 0

                    dp[row][col] = up + left

        return  dp[m-1][n-1]

            
