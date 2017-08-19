class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        last = nums[0]
        leng = 1
        for i in range(1, len(nums)):
            if nums[i] == last:
                continue
            else:
                nums[leng] = nums[i]
                leng += 1
                last = nums[i]
        print(nums[:leng])
        return leng

if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,2,3,5,5,6]))