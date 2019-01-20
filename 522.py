class Solution:

    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def common_sub_sequence(a, b):
            i, j = 0, 0

            while i < len(a) and j < len(b):
                j = b[j:].index(a[i])
                if not j:
                    return -1
                i += 1

        return -1


if __name__ == "__main__":
    print()