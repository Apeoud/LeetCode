class Solution(object):

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num_list = list(str.strip())
        if len(num_list) == 0:
            return 0
        signal = -1 if num_list[0] == '-' else 1

        num = 0
        if num_list[0] in ['+', '-']:
            del num_list[0]

        i = 0
        while i < len(num_list) and num_list[i].isdigit():
            num = num * 10 + ord(num_list[i]) - ord("0")
            i = i + 1

        return signal * min(2**31, num) if signal == -1 else min(2**31-1, num)


if __name__ == "__main__":
    a = Solution()
    print(a.myAtoi("123"))
