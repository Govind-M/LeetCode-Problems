class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(path):

            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(len(nums)):
                if nums[i] not in path :
                    path.append(nums[i])
                    backtracking(path)
                    path.pop()

        backtracking([])

        return result
