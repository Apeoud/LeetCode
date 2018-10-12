class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0
        begin = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] <= prices[begin]:
                begin = i
            else:
                profit += prices[i] - prices[begin]
                begin = i
        return profit

if __name__ == "__main__":
    print(Solution().maxProfit([7,6,4,3,1]))