class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []

        digint_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 1:
            return digint_map.get(digits[0], [""])
        else:
            res = []
            for s in self.letterCombinations(digits[1:]):
                for p in digint_map.get(digits[0], [""]):
                    res.append(p + s)
            return res

if __name__ == "__main__":
    print(Solution().letterCombinations("123"))