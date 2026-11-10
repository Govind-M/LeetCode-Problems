# from collections import deque
# class Solution:
#     def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
#         q = deque([source])
#         visited = {source}
#         graphMap = {}

#         for x,y in edges:
#             if x not in graphMap:
#                 graphMap[x] = []
#             if y not in graphMap:
#                 graphMap[y] = []
#             graphMap[x].append(y)
#             graphMap[y].append(x)

#         while len(q):
#             curr = q.popleft()

#             if curr == destination:
#                 return True
            
#             for neighbor in graphMap.get(curr,[]):
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     q.append(neighbor)
                    


#         return False


        


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        graphMap = {}
        for x,y in edges:
            if x not in graphMap:
                graphMap[x] = []
            if y not in graphMap:
                graphMap[y] = []

            graphMap[x].append(y)
            graphMap[y].append(x)

        visited = {source}

        def dfs(curr):
            
            if curr == destination:
                return True

            for neighbor in graphMap.get(curr,[]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor):
                        return True

            return False
        

        return dfs(source)

