from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.word = word

        for i in range(self.m):
            for j in range(self.n):
                if self.backtrace(i, j, 0):
                    return True

        return False

    def backtrace(self, x, y, count):
        # can not move anymore
        if x < 0 or y < 0 or x >= self.m or y >= self.n:
            return False

        # wrong char
        curr_ch = self.board[x][y]
        if curr_ch is None:
            return False

        if curr_ch != self.word[count]:
            return False

        # found
        if count == len(self.word) - 1:
            return True

        # tag
        self.board[x][y] = None

        # four directions
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if abs(i) + abs(j) != 1:
                    continue
                if self.backtrace(x + i, y + j, count + 1):
                    return True

        # revert tag
        self.board[x][y] = curr_ch

        return False

