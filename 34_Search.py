class Solution(object):
    def get(self, nums, mid):
        m = 1
        while mid + m < len(nums):
            if nums[mid + m] == nums[mid]:
                m += 1
            else:
                break
        n = 1
        while mid - n >= 0:
            if nums[mid - n] == nums[mid]:
                n += 1
            else:
                break
        return [mid - n + 1, mid + m - 1]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        begin, end = 0, len(nums) - 1
        while begin < end:
            if end - begin == 1:
                if nums[begin] == target:
                    return self.get(nums, begin)
                if nums[end] == target:
                    return self.get(nums, end)
                return [-1, -1]
            mid = int((begin + end) / 2)
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                begin = mid
            else:
                return self.get(nums, mid)
        if nums[begin] == target:
            return [begin, begin]
        return [-1, -1]


if __name__ == "__main__":
    print(Solution().searchRange([1,1,2], 1))
