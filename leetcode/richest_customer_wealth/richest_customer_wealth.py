from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            customer_wealth = sum(customer)
            if customer_wealth > max_wealth:
                max_wealth = customer_wealth
        return max_wealth

def main():
    s = Solution()
    print('[[1,2,3],[3,2,1]]:', s.maximumWealth([[1,2,3],[3,2,1]]))
    print('[[1,5],[7,3],[3,5]]:', s.maximumWealth([[1,5],[7,3],[3,5]]))
    print('[[2,8,7],[7,1,3],[1,9,5]]:', s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

if __name__ == '__main__':
    main()