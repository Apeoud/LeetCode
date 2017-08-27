class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        flag = []
        for e in nums:
            if e >= 0:
                if len(flag) == 0:
                    flag = [0] * (len(nums) + 2)

        for e in nums:
            if 0 < e < len(nums) + 2:
                flag[e-1] = 1

        for i in range(len(flag)):
            if flag[i] != 1:
                return i + 1

        return len(nums) + 2


if __name__ == "__main__":
    print(Solution().firstMissingPositive([0]))
