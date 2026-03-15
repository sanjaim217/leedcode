class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [[0 for _ in range(n)] for _ in range(n)]

        row_sums = [0 for _ in range(n)]
        col_sums = [0 for _ in range(n)]
        left_diag_sums = {}
        right_diag_sums = {}
        for i in range(n):
            left_diag_sums[(i, 0)] = 0
            left_diag_sums[(0, i)] = 0
            right_diag_sums[(i, n)] = 0
            right_diag_sums[(0, i)] = 0

        def _getLeftDiagonalIndex(i, j):
            offset = min(i, j)
            i_, j_ = i - offset, j - offset
            return (i_, j_)

        def _getRightDiagonalIndex(i, j):
            if i + j <= n:            
                i_, j_ = 0, j + i
            else:
                offset = n - j
                i_, j_ = i - offset, n
            return (i_, j_)

        def _validate(i, j):
            if all([
                row_sums[i] == 0, col_sums[j] == 0,
                left_diag_sums[_getLeftDiagonalIndex(i,j)] == 0,
                right_diag_sums[_getRightDiagonalIndex(i,j)] == 0
            ]):
                return True
            return False

        def _setState(i, j, status):
            board[i][j] = status
            row_sums[i] = status
            col_sums[j] = status
            left_diag_sums[_getLeftDiagonalIndex(i,j)] = status
            right_diag_sums[_getRightDiagonalIndex(i,j)] = status

        solutions = []
        def backtracking(i: int = 0, j: int = 0, remain: int = n):
            if remain == 0:
                # found a solution, add to list of solutions
                solution = []
                for i in range(n):
                    row = ""
                    for j in range(n):
                        if board[i][j] == 0:
                            row += "."
                        else:
                            row += "Q"
                    solution.append(row)
                solutions.append(solution)
                return
            if i >= n or j >= n:
                return

            if _validate(i, j):
                # Choice 1: Place the Queen
                _setState(i, j, 1) # move
                backtracking(i+1, 0, remain-1) # go to next row
                _setState(i, j, 0) # undo move

            # Choice 2: Not Place the Queen
            backtracking(i, j+1, remain) # move right

        backtracking()
        return solutions