class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # 用减法来实现除法不可行 会超时。。应该使用移位运算符
        # 技不如人 甘拜下风
        # discuss 答案

        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            mod, weight = divisor, 1
            while dividend >= mod:
                dividend -= mod
                res += weight
                weight <<= 1
                mod <<= 1

        res = res if sign else -res

        return min(max(-2 ** 31, res), 2 ** 31 -1)


if __name__ == "__main__":
    print(Solution().divide(-2147483648, -1))
