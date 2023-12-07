from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
        
def main():
    s = Solution()
    print('prices = [7,1,5,3,6,4]:', s.maxProfit(prices = [7,1,5,3,6,4]))
    print('prices = [7,6,4,3,1]:', s.maxProfit(prices = [7,6,4,3,1]))

if __name__ == '__main__':
    main()