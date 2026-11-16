class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i , j = 0, 0
        currLen = 0
        minLen = float("inf")
        currSum = 0

        while j < len(nums):
            currSum += nums[j]

            while currSum >= target:
                currLen = (j-i) + 1
                minLen = min(minLen, currLen)

                currSum -= nums[i]
                i +=1
            
            j += 1

        return 0 if minLen == float("inf") else minLen