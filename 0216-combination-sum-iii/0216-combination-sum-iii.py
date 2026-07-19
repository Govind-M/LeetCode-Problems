class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(targetSum, path, startNum):

            if len(path) == k and targetSum == 0:
                result.append(list(path))
                return

            if targetSum <=0:
                return

            for i in range(startNum,10):
                path.append(i)
                backtrack(targetSum-i, path, i+1)
                path.pop()

            
        backtrack(n, [], 1)
        return result