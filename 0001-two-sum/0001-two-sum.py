class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target

        n = len(self.nums)
        seen = {}

        for i in range(n):
            if self.target-nums[i] in seen:
                return [i,seen[target-nums[i]]]
            elif nums[i] not in seen:
                seen[nums[i]] = i
            

        return []