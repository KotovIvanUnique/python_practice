from typing import List

class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     result = set()
    #     for i in range(len(nums) - 2):
    #         if nums[i] + nums[i + 1] + nums[i + 2] == 0:
    #             result.add((nums[i], nums[i + 1], nums[i + 2]))
    #     return list(map(list, list(result)))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        num_counts = {num: nums.count(num) for num in nums}
        for key, value in num_counts():
            result.add((nums[i], nums[i + 1], nums[i + 2]))
        return list(map(list, list(result)))
        
def main():
    s = Solution()
    print('[-1,0,1,2,-1,-4]:', s.threeSum([-1,0,1,2,-1,-4]))
    print('[0,1,1]:', s.threeSum([0,1,1]))
    print('[0,0,0]:', s.threeSum([0,0,0]))

if __name__ == '__main__':
    main()