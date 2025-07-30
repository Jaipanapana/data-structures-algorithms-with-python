class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length=len(prices)
        i=1
        prefix=[0]*len(prices)
        prefix[0]=prices[0]
        while(i<length):
            prefix[i]=min(prefix[i-1],prices[i])
            i+=1
        i=1
        while(i<length):
            buy=prefix[i]
            if prices[i]-buy>profit :
                profit=prices[i]-buy
            i+=1
        return profit
        
