# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

from typing import List


# 贪心算法：已知所有交易日的价格，每个上涨交易日都做买卖，下降交易日都不买卖，相当于汇总所有递增区间即为最大利润，汇总所有递减区间即为最大亏损
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit
