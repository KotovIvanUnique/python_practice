from typing import List

class Solution:
    def __get_median(self, nums: List[int]) -> float:
        middle = len(nums) // 2
        if len(nums)%2 == 0:
            return float((nums[middle-1] + nums[middle])/2)
        else:
            return float(nums[middle])

    def __get_idx(self, nums: List[int], num: int) -> int:
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] < num and i+1 < len_nums and nums[i + 1] >= num:
                return i + 1
            elif nums[i] < num and i+1 == len_nums:
                return i + 1
            elif i == 0 and nums[i] >= num:
                return 0

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            idx = self.__get_idx(nums1, i)
            nums1 = nums1[:idx] + [i] + nums1[idx:]
        return self.__get_median(nums1)

def main():
    s = Solution()
    print('nums1 = [1,3], nums2 = [2]:', s.findMedianSortedArrays([1,3], [2]))
    print('nums1 = [1,2], nums2 = [3,4]:', s.findMedianSortedArrays([1,2], [3,4]))

if __name__ == '__main__':
    main()