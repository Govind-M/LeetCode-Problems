class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        
        left = 0
        totalSum = 0
        subArrays = 0
        currAvg = 0

        for right in range(len(arr)):

            totalSum += arr[right]

            if (right-left) + 1 > k:

                totalSum -= arr[left]
                left += 1

            if (right-left) + 1 == k:

                currAvg = totalSum/k

                if currAvg >= threshold:
                    subArrays += 1

        return subArrays

