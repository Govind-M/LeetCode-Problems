# // Top-DOwn Recursive Solution with memoization


# class Solution:
#     def rob(self, nums: list[int]) -> int:
        
#         dp = {}

#         def fn(n):

#             if n == 0:
#                 return nums[0]

#             if n == 1:
#                 return max(nums[0],nums[1])

#             if n in dp:
#                 return dp[n]

#             dp[n] = max(fn(n-2)+nums[n], fn(n-1))

#             return dp[n]

#         return fn(len(nums)-1)


# Bottom up tabulation method

# class Solution:
#     def rob(self, nums: list[int]) -> int:

#         dp = {}

#         if len(nums) == 1:
#             return nums[0]

#         dp[0] = nums[0]
#         dp[1] = max(nums[0],nums[1])

#         for i in range(2,len(nums)):
#             dp[i] = max(dp[i-2]+nums[i],dp[i-1])

#         print(dp)

        
#         return dp[len(nums)-1]



# space optimised solution

class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        p2 = nums[0] 
        p1 = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            curr = max(p2 + nums[i], p1)
            temp = p1
            p1 = curr
            p2 = temp
            curr += 1


        
        return p1