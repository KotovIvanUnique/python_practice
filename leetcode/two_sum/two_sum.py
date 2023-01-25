from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

def main():
    s = Solution()
    print('nums = [2,7,11,15], target = 9:', s.twoSum([2,7,11,15], 9))
    print('nums = [3,2,4], target = 6:', s.twoSum([3,2,4], 6))
    print('nums = [3,3], target = 6:', s.twoSum([3,3], 6))

if __name__ == '__main__':
    main()