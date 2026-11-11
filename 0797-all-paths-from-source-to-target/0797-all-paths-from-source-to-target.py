class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        
        start = 0
        end = len(graph)-1

        allPaths = []

        def dfs(curr, path):

            if curr == end:
                allPaths.append(path.copy())
                return

            for n in graph[curr]:
                path.append(n)
                dfs(n,path)
                path.pop()

        dfs(start,[start])

        return allPaths