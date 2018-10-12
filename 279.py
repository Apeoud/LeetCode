import math


class Solution(object):
    saved = dict()

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        max_num = int(math.sqrt(n))

        if n in self.saved.keys():
            return self.saved[n]

        if n == pow(max_num, 2):
            self.saved[n] = 1
            return 1

        min_num = 1000000000000
        index = max_num
        while index > 0:
            cur = 1 + self.numSquares(n - index * index)
            if cur == 2:
                min_num = cur
                break
            if cur < min_num:
                min_num = cur
            index -= 1

        self.saved[n] = min_num
        return min_num


if __name__ == "__main__":
    print(Solution().numSquares(7168))
