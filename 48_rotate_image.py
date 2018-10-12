class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # implement a map from (i,j) to (j,n-i) n-i n -j n-j i i j

        n = len(matrix)

        for i in range(int(n / 2 + 0.5)):
            for j in range(i, int((n - i)) - 1 ):
                begin = matrix[i][j]

                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = begin
        print(matrix)
        return matrix


if __name__ == "__main__":
    sol = Solution()

    c = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]

    c2 = [[1, 2], [3, 4]]

    print(sol.rotate(c))
