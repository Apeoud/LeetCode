import math


class Solution(object):
    saved = dict()

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        base = []
        while i * i <= n:
            base.append(i * i)
            i += 1

        index = 1

        tmp = base

        while True:
            new_tmp = set()
            for k in tmp:
                if n == k:
                    return index
                for b in base:
                    new_tmp.add(k + b)

            tmp = new_tmp

            index += 1


if __name__ == "__main__":
    print(Solution().numSquares(12))
