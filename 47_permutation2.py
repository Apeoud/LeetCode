class Solution(object):
    saved = set()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def hash(l):
            res = ""
            for ele in l:
                res += str(ele) + "_"
            return res[:-1]

        def dehash(h):
            return [int(k) for k in h.split("_")]

        def subf(num):
            if len(num) == 0:
                return []

            if len(num) == 1:
                return [str(num[0])]

            res = set()

            for k in range(len(num)):
                left = num[:k] + num[k + 1:]

                for re in subf(left):
                    res.add(str(num[k]) + "_" + re)

            return res

        return [dehash(s) for s in subf(nums)]


if __name__ == "__main__":
    sol = Solution()

    print(sol.permute([-1, 2]))
