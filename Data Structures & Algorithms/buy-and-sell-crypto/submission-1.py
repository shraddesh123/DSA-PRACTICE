class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        n=len(prices)
        i=0
        for j in range(n):
            current=prices[j]-prices[i]
            maximum=max(current,maximum)

            if prices[i]>prices[j]:
                i=j



        return maximum