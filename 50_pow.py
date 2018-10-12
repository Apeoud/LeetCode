class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """



        if n == 0:
            return 1

        if x == 0:
            return 0

        if n < 0 :
            x = 1/x
            n = -n

        res = 1

        for _ in n:
            res = res * x

if __name__ == "__main__":
    print(pow())