class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(targetSum, path,start):

            if targetSum == 0:
                result.append(list(path))
                return
            
            if targetSum <= 0 :
                return

            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(targetSum-candidates[i],path,i+1)
                path.pop()

            
        backtrack(target,[],0)

        return result

            