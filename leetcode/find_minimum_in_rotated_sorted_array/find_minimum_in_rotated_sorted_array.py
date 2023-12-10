from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_idx, right_idx = 0, len(nums) - 1
        curr_min = 9223372036854775807

        while left_idx < right_idx:
            mid_idx = (left_idx + right_idx) // 2
            curr_min = min(curr_min, nums[mid_idx])

            if nums[mid_idx] > nums[right_idx]:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1

        return min(curr_min, nums[left_idx])
        
def main():
    s = Solution()
    print('nums = [3,4,5,1,2]:', s.findMin(nums = [3,4,5,1,2]))
    print('nums = [4,5,6,7,0,1,2]:', s.findMin(nums = [4,5,6,7,0,1,2]))
    print('nums = [11,13,15,17]:', s.findMin(nums = [11,13,15,17]))
    print('nums = [4,5,6,7,0,1,2]:', s.findMin(nums = [8,9,10,11,0,1,2,3,4,5,6,7]))

if __name__ == '__main__':
    main()