import time


class Solution(object):
    times = 0
    cache = dict()

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        sp_id = "%s_%s" % (s, p)

        if sp_id in self.cache.keys():
            self.times += 1
            return self.cache[sp_id]

        # s == 0 的情况
        if len(s) == 0:
            for e in p:
                if e != "*":
                    self.cache[sp_id] = False
                    return False
            self.cache[sp_id] = True
            return True
        i = 0
        j = 0
        while i < len(p) and j < len(s):
            if p[i] == "*":
                i += 1
                while i < len(p) and p[i] == "*":
                    i += 1
                if i == len(p):
                    self.cache[sp_id] = True
                    return True
                while j < len(s):
                    if s[j] == p[i] or p[i] == "?":
                        if self.isMatch(s[j:], p[i:]):
                            self.cache[sp_id] = True
                            return True
                    j += 1
            elif p[i] == "?":
                i += 1
                j += 1
            else:
                if s[j] == p[i]:
                    j += 1
                    i += 1
                else:
                    self.cache[sp_id] = False
                    return False
        if i == len(p) and j == len(s):

            self.cache[sp_id] = True
            return True
        elif i < len(p) and j == len(s):
            for e in p[i:]:
                if e != "*":
                    self.cache[sp_id] = False
                    return False

            self.cache[sp_id] = True
            return True
        else:
            self.cache[sp_id] = False
            return False


if __name__ == "__main__":
    sol = Solution()

    bt = time.time()
    print(sol.isMatch(
        "abbbabaaabbabbabbabaabbbaabaaaabbbabaaabbbbbaaababbb",
        "**a*b*aa***b***bbb*ba*a"))

    et = time.time()

    print(et - bt)
    print(sol.times)


