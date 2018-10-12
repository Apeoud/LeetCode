class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        reserve = dict()

        def dfs(s, wordDict, start):

            if start in reserve.keys():
                return reserve[start]

            final = []

            alternative = []

            for word in wordDict:
                if len(word) <= len(s) and s[:len(word)] == word:
                    alternative.append(word)

            if not len(alternative):
                return None

            for alt in alternative:
                if len(alt) == len(s):
                    final.append([alt])
                    continue

                next = dfs(s[len(alt):], wordDict, start + len(alt))
                if next:
                    for t in next:
                        final.append([alt] + t)
            reserve[start] = final
            return final

        re = dfs(s, wordDict, 0)
        if not re:
            return []

        return [' '.join(s) for s in re]


if __name__ == "__main__":
    print(Solution().wordBreak("aaa", ["a", "aa"]))
