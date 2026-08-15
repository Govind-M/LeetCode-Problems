class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.']*n for _ in range(n)]

        def backtrack(board, row, colSet, digSet, antiDigSet):

            if row == n:
                    result.append([''.join(r) for r in board])
                    return


            for col in range(n):

                if col in colSet or (row-col) in digSet or (row+col) in antiDigSet:
                    continue
                
                board[row][col] = "Q"
                colSet.add(col)
                digSet.add(row-col)
                antiDigSet.add(row+col)
                backtrack(board, row+1, colSet, digSet, antiDigSet)
                board[row][col] = '.'
                colSet.remove(col)
                digSet.remove(row-col)
                antiDigSet.remove(row+col)

        backtrack(board, 0, set(), set(), set())
        return result  

        