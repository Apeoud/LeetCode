class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        cache = dict()

        def match(s, p):
            sp_id = "%s_%s" % (s, p)

            if sp_id in cache.keys():
                return cache[sp_id]

            # s == 0 的情况
            if len(s) == 0:
                for e in p:
                    if e != "*":
                        cache[sp_id] = False
                        return False
                cache[sp_id] = True
                return True
            i = 0
            j = 0
            while i < len(p) and j < len(s):
                if p[i] == "*":
                    i += 1
                    while i < len(p) and p[i] == "*":
                        i += 1
                    if i == len(p):
                        cache[sp_id] = True
                        return True
                    while j < len(s):
                        if s[j] == p[i] or p[i] == "?":
                            if match(s[j:], p[i:]):
                                cache[sp_id] = True
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
                        cache[sp_id] = False
                        return False
            if i == len(p) and j == len(s):

                cache[sp_id] = True
                return True
            elif i < len(p) and j == len(s):
                for e in p[i:]:
                    if e != "*":
                        cache[sp_id] = False
                        return False

                cache[sp_id] = True
                return True
            else:
                cache[sp_id] = False
                return False

        return match(s, p)


if __name__ == "__main__":
    print(Solution().isMatch("aa", "*"))
