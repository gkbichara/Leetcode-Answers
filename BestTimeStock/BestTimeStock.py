class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_cur = 10000000
        max_sum = 0
        temp = 0
        while temp < len(prices):
            if prices[temp] < min_cur:
                min_cur = prices[temp]
                temp += 1
                continue
            else:
                cur_dif = prices[temp] - min_cur
                max_sum = max(max_sum, cur_dif)
                temp += 1
                continue

        return max_sum