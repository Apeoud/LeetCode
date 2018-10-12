class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        # 第一种解法，先找个每个C，然后分别计算每个字符到每个C的距离，取最小值
        # C_position = []
        #
        # for i, e in enumerate(S):
        #     if e == C:
        #         C_position.append(i)
        #
        # return [min(abs(i - s) for s in C_position) for i, e in enumerate(S)]

        # 第二种解法，双向扫描
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestToChar("loveleetcode"
                             , "e"))
