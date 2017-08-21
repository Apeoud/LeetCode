class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        bef = self.countAndSay(n - 1)
        cur = bef[0]
        count = 0
        res = ""
        for char in bef:
            if char == cur:
                count += 1
            else:
                res += str(count) + str(cur)
                cur = char
                count = 1
        res += str(count) + str(cur)
        return res


if __name__ == "__main__":
    print(Solution().countAndSay(5))
