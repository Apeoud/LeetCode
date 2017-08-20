class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columes = []
        subs = []
        for row in board:
            if len([e for e in row if e != "."]) != len(set(row)) - 1:
                return False
        for i in range(9):
            column = [row[i] for row in board]
            columes.append(column)
            if len([e for e in column if e != "."]) != len(set(column)) - 1:
                return False
        for i in range(3):
            for j in range(3):
                sub = board[i * 3][j * 3:(j+1) * 3] + board[i * 3 + 1][j * 3:(j+1) * 3] + board[i * 3 + 2][j * 3:(j+1) * 3 ]
                subs.append(sub)
                if len([e for e in sub if e != "."]) != len(set(sub)) - 1:
                    return False

        possibility = []
        for i in range(9):
            prob_row = []
            for j in range(9):
                if board[i][j] == ".":
                    prob_row.append([str(e) for e in range(1,10) if str(e) not in list(board[i])])
                else:
                    prob_row.append([board[i][j]])
            possibility.append(prob_row)

        for i in range(9):
            for j in range(9):
                if columes[i][j] == ".":
                    possibility[j][i] = [e for e in possibility[j][i] if e not in list(columes[i])]

        for i in range(9):
            for j in range(9):
                if subs[i][j] == ".":
                    rown = int(i / 3 + j / 3)
                    columnn = int(i % 3 * 3 + j % 3)
                    possibility[rown][columnn] = [e for e in possibility[j][i] if e not in list(subs[i])]

        print(possibility)

        for r in possibility:
            for c in r:
                if len(c) == 0:
                    return False

        return True


if __name__ == "__main__":
    board = [".87654321", "2........", "3........", "4........", "5........",
             "6........", "7........", "8........", "9........"]
    Solution().isValidSudoku(board=board)
