from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        return [x[0] for x in list(sorted(counts.items(), key=lambda x: x[1], reverse=True))[:k]]

def main():
    s = Solution()
    print('nums = [1,1,1,2,2,3], k = 2:', s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print('nums = [1], k = 1:', s.topKFrequent(nums = [1], k = 1))

if __name__ == '__main__':
    main()