class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        m = len(board)
        n = len(board[0])

        def backtrack(x, y, nextIndex):

            if nextIndex == len(word):
                self.result = True
                return

            original = board[x][y]
            board[x][y] = '#'
            
            if y>0 and board[x][y-1] == word[nextIndex]:
                backtrack(x, y-1, nextIndex+1)
            
            if y<n-1 and board[x][y+1] == word[nextIndex]:
                backtrack(x, y+1, nextIndex+1)

            if x>0 and board[x-1][y] == word[nextIndex]:
                backtrack(x-1, y, nextIndex+1)

            if x<m-1 and board[x+1][y] == word[nextIndex]:
                backtrack(x+1, y, nextIndex+1)

            board[x][y] = original

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    backtrack(i,j,1)
                    if self.result:
                        return True

        return self.result
            