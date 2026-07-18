class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remainingSum, path, start):

            if remainingSum == 0:
                result.append(list(path))

            if remainingSum <=0:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(remainingSum-candidates[i], path, i)
                path.pop()

        
        backtrack(target,[],0)

        return result