class Solution(object):
    def copy(self, poss):
        res = []
        for row in poss:
            res_row = []
            for e in row:
                res_row.append(list(e) if isinstance(e, list) else e)
            res.append(res_row)
        return res

    def check_bug(self, poss):
        for i in range(9):
            for j in range(9):
                if isinstance(poss[i][j], list) and len(poss[i][j]) == 0:
                    return False
        return True

    def update(self, poss):
        flag = True
        while flag:
            flag = False
            for i in range(len(poss)):
                for j in range(len(poss[i])):
                    # 如果可能性只降到一个 就赋值

                    if isinstance(poss[i][j], list) and len(poss[i][j]) == 1:
                        poss[i][j] = poss[i][j][0]
                        flag = True
                    # 赋值完后 对可能被影响的其他的区域更新
                    # row
                    for pos_row in poss[i]:
                        if isinstance(pos_row, list) and poss[i][j] in pos_row:
                            pos_row.remove(poss[i][j])
                    # column
                    for c in range(9):
                        if isinstance(poss[c][j], list) and poss[i][j] in poss[c][j]:
                            poss[c][j].remove(poss[i][j])
                    # sub
                    sub_row = range(int(i / 3) * 3, int(i / 3) * 3 + 3)
                    sub_column = range(int(j / 3) * 3, int(j / 3) * 3 + 3)
                    for sub_i in sub_row:
                        for sub_j in sub_column:
                            if isinstance(poss[sub_i][sub_j], list) and \
                                            poss[i][j] in poss[sub_i][sub_j]:
                                poss[sub_i][sub_j].remove(poss[i][j])
        for i in range(9):
            for j in range(9):
                if isinstance(poss[i][j], list) and len(poss[i][j]) == 0:
                    return False
        return True

    def check_void(self, poss):
        for i in range(len(poss)):
            for j in range(len(poss[i])):
                if len(poss[i][j]) != 1:
                    return False
        return True

    def assumption(self, poss):
        for i in range(len(poss)):
            for j in range(len(poss[i])):
                if len(poss[i][j]) == 2:
                    tmp = poss[i][j][1]
                    poss[i][j] = poss[i][j][0]
                    return [i, j, tmp, poss[i][j]]
        return False

    def cover(self, poss, board):
        for i in range(9):
            board[i] = ''.join(poss[i])

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        columes = []
        subs = []
        for i in range(9):
            column = [row[i] for row in board]
            columes.append(column)

        for i in range(3):
            for j in range(3):
                sub = board[i * 3][j * 3:(j + 1) * 3] + board[i * 3 + 1][j * 3:(j + 1) * 3] + board[i * 3 + 2][
                                                                                              j * 3:(j + 1) * 3]
                subs.append(sub)

        possibility = []
        for i in range(9):
            prob_row = []
            for j in range(9):
                if board[i][j] == ".":
                    prob_row.append([str(e) for e in range(1, 10) if str(e) not in list(board[i])])
                else:
                    prob_row.append(board[i][j])
            possibility.append(prob_row)

        for i in range(9):
            for j in range(9):
                if columes[i][j] == ".":
                    possibility[j][i] = [e for e in possibility[j][i] if e not in list(columes[i])]

        for i in range(9):
            for j in range(9):
                if subs[i][j] == ".":
                    rown = int(int(i / 3) * 3 + j / 3)
                    columnn = int(i % 3 * 3 + j % 3)
                    possibility[rown][columnn] = [e for e in possibility[rown][columnn] if e not in list(subs[i])]

        # print_prob(possibility)
        self.update(possibility)
        print("第一次消歧后")
        # print_prob(possibility)

        if self.check_void(possibility):
            self.cover(possibility, board)
            return

        stack = []
        stack_prob = []
        copy = self.copy(possibility)
        while True:
            res = self.assumption(copy)
            backup = self.copy(copy)

            if isinstance(res, list):
                stack.append(res)
                stack_prob.append(backup)
                if not self.update(copy):
                    # 消除假设
                    while not self.check_bug(copy):
                        if len(stack) <= 0:
                            break

                        tmp = stack[-1]
                        copy = stack_prob[-1]
                        copy[tmp[0]][tmp[1]] = tmp[2]

                        # for mid in stack[:-1]:
                        #     copy[mid[0]][mid[1]] = mid[3]
                        #     self.update(copy)
                        stack = stack[:-1]
                        stack_prob = stack_prob[:-1]
                        self.update(copy)
                        # print_prob(copy)
                    if self.check_void(copy):
                        self.cover(copy, board)
                        return

                else:
                    # 判断是否成功
                    if self.check_void(copy):
                        self.cover(copy, board)
                        return
            else:
                tmp = stack[-1]
                copy = self.copy(possibility)
                copy[tmp[0]][tmp[1]] = tmp[2]
                # print_prob(copy)
                self.update(copy)
                stack = []
                if self.check_void(copy):
                    self.cover(copy, board)
                    return


def printSudoku(board):
    for row in board:
        print(' '.join(row))
    print("\n")


def print_prob(poss):
    for row in poss:
        tmp = []
        for ele in row:
            if len(ele) == 1:
                tmp.append(ele[0])
            else:
                tmp.append('.')
        print(' '.join(tmp))
    print('\n')


if __name__ == "__main__":
    board = [".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
    printSudoku(board)
    Solution().solveSudoku(board)
    print("最终结果")
    printSudoku(board)
