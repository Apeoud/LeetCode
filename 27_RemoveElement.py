class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i:] = nums[i+1:]
            else:
                i += 1
        print(nums)
        return len(nums)

if __name__ == "__main__":
    print(Solution().removeElement([1], 2))