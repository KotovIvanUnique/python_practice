from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_sum = 0
        left = k
        n = len(cardPoints)
        right = n
        sum_left = sum(cardPoints[:left])
        sum_right = 0
        while n - right <= k:
            max_sum = max(max_sum, sum_left + sum_right)
            left -= 1
            right -= 1
            sum_left = sum_left - cardPoints[left]
            sum_right = sum_right + cardPoints[right]
        return max_sum

def main():
    s = Solution()
    print('cardPoints = [1,2,3,4,5,6,1], k = 3:', s.maxScore([1,2,3,4,5,6,1], 3))
    print('cardPoints = [2,2,2], k = 2:', s.maxScore([2,2,2], 2))
    print('cardPoints = [9,7,7,9,7,7,9], k = 7:', s.maxScore([9,7,7,9,7,7,9], 7))

if __name__ == '__main__':
    main()