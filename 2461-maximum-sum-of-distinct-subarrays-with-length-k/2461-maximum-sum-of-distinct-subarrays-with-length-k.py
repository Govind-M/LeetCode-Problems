class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        
        left = 0
        currSum = 0
        maxSum = 0
        numDict = {}

        for right in range(len(nums)):

            if nums[right] not in numDict:
                numDict[nums[right]] = 1
            else:
                numDict[nums[right]] += 1

            currSum += nums[right]

            if (right-left) + 1 > k:
                currSum -= nums[left]
                
                numDict[nums[left]] -= 1

                if numDict[nums[left]] == 0:
                    numDict.pop(nums[left])

                left +=1

            if (right-left) + 1 == k and len(numDict) == k:
                maxSum = max(maxSum, currSum)

        return maxSum