class Solution:
    def maxProfit(self, prices):
        '''
        type price: List[int]
        rtype: int
        '''
        maxprofit = 0
        if (len(prices) == 0):
            return 0
        for i in range(0, len(prices)-1):     # 遍歷一次, 只要明天的價格高於今天就算進去, 累積小營收
            if(prices[i+1] > prices[i]):
                maxprofit += prices[i+1]-prices[i]
        return maxprofit

data = [7,1,5,3,6,4]
s = Solution()

print(s.maxProfit(data))        