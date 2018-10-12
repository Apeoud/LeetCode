class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        beg = 0
        end = len(nums) - 1

        while beg < end:
            mid = int((beg + end) / 2)
            if target == nums[mid]:
                return True

            if nums[mid] > nums[beg]:
                if target > nums[mid] or target < nums[beg]:
                    beg
