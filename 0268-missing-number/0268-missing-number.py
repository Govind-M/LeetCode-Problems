class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sumNum = 0
        actualSumNum = 0

        for i in range(len(nums)):
            sumNum += nums[i]
        
        for i in range(len(nums) + 1):
            actualSumNum += i

        return actualSumNum - sumNum