from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        n = len(nums)
        if n < 2:
            return 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    c += 1
        return c

def main():
    s = Solution()
    print('[1,2,3,1,1,3]:', s.numIdenticalPairs([1,2,3,1,1,3]))
    print('[1,1,1,1]:', s.numIdenticalPairs([1,1,1,1]))
    print('[1,2,3]:', s.numIdenticalPairs([1,2,3]))

if __name__ == '__main__':
    main()