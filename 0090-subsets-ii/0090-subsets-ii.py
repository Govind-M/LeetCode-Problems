class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtracking(path,start):
            result.append(list(path))

            for i in range(start,len(nums)):
                if nums[i-1] == nums[i] and i > start:
                    continue
                
                path.append(nums[i])
                backtracking(path,i+1)
                path.pop()


        backtracking([],0)

        return result