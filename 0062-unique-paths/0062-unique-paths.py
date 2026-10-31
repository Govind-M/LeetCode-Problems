class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def fn(row,col):
            
            if row == 0 and col == 0:
                return 1
            
            if row < 0 or col < 0:
                return 0

            if (row,col) in dp:
                return dp[(row,col)]
            
            up = fn(row-1, col)
            left = fn(row, col-1)
            dp[(row,col)] = up + left

            return up + left

        return fn(m-1, n-1)
            
