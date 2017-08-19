class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def correct(s1, s2):
            if s1 == "{":
                return True if s2 == "}" else False
            if s1 == "(":
                return True if s2 == ")" else False
            if s1 == "[":
                return True if s2 == "]" else False
            return False

        if len(s) == 0:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            # i, j = int(len(s) / 2 - 1), int(len(s) / 2)
            # while i >= 0:
            #     if not correct(s[i], s[j]):
            #         return False
            #     i, j = i - 1, j + 1
            # return True
            bef = []
            for c in s:
                if c in ["{", "(", "["]:
                    bef.append(c)
                else:
                    if len(bef) == 0:
                        return False
                    if correct(bef[-1], c):
                        bef = bef[:-1]
                    else:
                        return False
            return True if len(bef) == 0 else False


if __name__ == "__main__":

    print(Solution().isValid("[([]])"))
