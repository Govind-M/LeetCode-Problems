
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        q = deque([node])
        visited = {}

        clonedRoot = Node(node.val)
        visited[node] = clonedRoot

        while len(q):
            curr = q.popleft()
            clonedCurr = visited[curr]

            for n in curr.neighbors:
                if n not in visited:
                    q.append(n)
                    visited[n] = Node(n.val)
                clonedCurr.neighbors.append(visited[n])

        return  clonedRoot
        

