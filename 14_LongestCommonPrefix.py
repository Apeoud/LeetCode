class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        lcp = strs[0]

        def compare(s1, s2):
            if s1 == s2 :
                return s1
            leng = min(len(s1), len(s2))
            if leng == 0:
                return ""

            for i in range(leng):
                if s1[i] != s2[i]:
                    return s1[:i]
            return s1[:leng]

        for s in strs[1:]:
            lcp = compare(lcp, s)
            if lcp == "":
                break

        return lcp

if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["aaa","aa","aaa"]))