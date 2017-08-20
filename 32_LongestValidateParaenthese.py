class Solution(object):
    def get(self, s):
        i = len(s) - 1
        l, r = 0, 0
        save = 0
        while i >= 0:
            if s[i] == ")":
                r += 1
                i -= 1
                while r >= l:
                    if s[i] == ")":
                        r += 1
                    else:
                        l += 1
                        if r < l:
                            save = r if r > save else save
                            r, l = 0, 0
                            break

                    i -= 1
            i -= 1
        return save

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        l = 0
        r = 0
        bef = 0
        opt = 0
        while i < len(s):
            if s[i] == "(":
                l += 1
            else:
                r += 1
                if r == l:
                    opt += r
                    r = 0
                    l = 0
                elif r > l:
                    bef = opt if opt > bef else bef
                    r = 0
                    l = 0
                    opt = 0
            i += 1
        if r >= l:
            return max(bef, opt) * 2
        else:
            return max(opt, bef, self.get(s[len(s) - r - l:])) * 2


if __name__ == "__main__":
    print(Solution().longestValidParentheses("(()(((()"))
