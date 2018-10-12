class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        res = []

        for k in range(len(nums)):
            left = nums[:k] + nums[k+1:]

            for re in self.permute(left):
                res.append([nums[k]] + re)

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.permute([1,1]))