class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        x = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[x]
                nums[x] = nums[i]
                nums[i] = temp

                x += 1        

        return  nums

        