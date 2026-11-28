class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        maxAvg = float("-inf")
        currAvg = 0
        totalSum = 0

        for right in range(len(nums)):

            totalSum += nums[right]

            if (right-left) + 1 > k:

                totalSum -= nums[left]
                left += 1

            if (right-left) + 1 == k:

                currAvg = totalSum/k
                maxAvg = max(maxAvg,currAvg)

        return maxAvg
