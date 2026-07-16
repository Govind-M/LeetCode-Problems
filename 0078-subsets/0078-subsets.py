class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(path,start):
            result.append(list(path))
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtracking(path, i+1)
                path.pop()
        
        backtracking([], 0)
        return result
        