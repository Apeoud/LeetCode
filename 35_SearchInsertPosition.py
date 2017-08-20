class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        begin, end = 0, len(nums) - 1
        if target < nums[begin]:
            return 0
        if target > nums[end]:
            return len(nums)
        while begin < end:
            if end - begin == 1:
                if nums[begin] == target:
                    return begin
                if nums[end] == target:
                    return end
                if target > nums[end]:
                    return end + 1
                if target < nums[begin]:
                    return begin
                else:
                    return end
            mid = int((begin + end) / 2)
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                begin = mid
            else:
                return mid


if __name__ == "__main__":
    print(Solution().searchInsert([1, 2, 3, 4, 5, 7, 8, 9, 10], 6))
