class Solution(object):
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        fb = sorted(nums)
        result = []
        for i in range(len(fb) - 2):
            if i >= 1 and fb[i] == fb[i - 1]:
                continue
            begin, end = i + 1, len(fb) - 1
            while begin < end:
                s = fb[i] + fb[begin] + fb[end]
                if s > target:
                    end -= 1
                elif s < target:
                    begin += 1
                else:
                    result.append([fb[i], fb[begin], fb[end]])

                    while begin < end and fb[begin + 1] == fb[begin]:
                        begin += 1
                    while end > begin and fb[end] == fb[end - 1]:
                        end -= 1
                    begin += 1
                    end -= 1

        return result

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        fb = sorted(nums)
        result = []
        for i in range(len(fb) - 3):
            if i >= 1 and fb[i] == fb[i - 1]:
                continue
            result += [[fb[i]] + k for k in self.threeSum(fb[i+1:], target-fb[i])]
        return result


if __name__ == "__main__":
    print(Solution().fourSum([0,0,0,0], 1))
