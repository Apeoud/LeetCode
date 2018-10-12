class Solution(object):
    def rerange(self, nums):
        for i in range(int(len(nums) / 2)):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= nums[i + 1]:
                i -= 1
            else:
                tmp = nums[i]
                j = i + 1
                while j < len(nums):
                    if nums[j] > tmp:
                        j += 1
                    else:
                        break
                nums[i], nums[j-1] = nums[j-1], nums[i]

                for k in range(int(len(nums[i+1:]) / 2)):
                    nums[i+1+k], nums[i+1+len(nums[i+1:]) - k - 1] = nums[i+1+len(nums[i+1:]) - k - 1], nums[i+1+k]
                print(nums)
                return
        for j in range(int(len(nums) / 2)):
            nums[j], nums[len(nums) - j - 1] = nums[len(nums) - j - 1], nums[j]
        print(nums)


if __name__ == "__main__":
    Solution().nextPermutation([5,1,1])
