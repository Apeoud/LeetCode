class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # if n < 1:
        #     return []
        # elif n == 1:
        #     return ["()"]
        # elif n == 2:
        #     return ["(())", "()()"]
        # else:
        #     res = []
        #     for s in self.generateParenthesis(n - 1):
        #         res += ["(" + s + ")", s + "()", "()" + s]
        #     res.remove("()" * n)
        #     return res
        res = ['(']
        i = 0
        while i < 2 * n - 1:
            i += 1
            tmp =[]
            for s in res:

                l = n - list(s).count("(")
                r = n - list(s).count(")")
                if l == 0:
                    tmp.append(s + ")")

                elif l > 0 and n > 0:
                    if l < r:
                        tmp.append(s + "(")
                        tmp.append(s + ")")

                    else:
                        tmp.append(s + "(")
            res = tmp
        return res


if __name__ == "__main__":
    print(len(Solution().generateParenthesis(4)))
