class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        fb = sorted(nums)
        cp = fb[0] + fb[1] + fb[2]
        for i in range(len(fb) - 2):
            if i >= 1 and fb[i] == fb[i - 1]:
                continue
            begin, end = i + 1, len(fb) - 1
            while begin < end:
                s = fb[i] + fb[begin] + fb[end]
                if s > target:
                    cp = cp if abs(cp - target) < abs(s - target) else s
                    end -= 1
                elif s < target:
                    begin += 1
                    cp = cp if abs(cp - target) < abs(s - target) else s
                else:
                    return target

        return cp


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
