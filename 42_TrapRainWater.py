class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0
        begin = 0
        trap = 0
        for i in range(1, len(height)):
            if height[i] >= height[begin]:
                trap += sum(height[begin] - e for e in height[begin:i])
                begin = i
            else:
                if height[i] > height[i - 1]:
                    j = i - 1
                    while j >= 0 and height[j] < height[i]:
                        j -= 1
                    trap += sum(height[i] - e for e in height[j + 1:i])
                    for k in range(j + 1, i):
                        height[k] = height[i]

        return trap


if __name__ == "__main__":
    print(Solution().trap([4, 2, 3]))
