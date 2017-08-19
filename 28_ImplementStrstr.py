class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(haystack) - len(needle)
        if length < 0:
            return -1
        else:
            for i in range(length+1):
                if haystack[i:i+(len(needle))] == needle:
                    return i
            return -1

if __name__ == "__main__":
    print(Solution().strStr("a", ""))