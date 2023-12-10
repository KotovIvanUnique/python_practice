from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        
def main():
    s = Solution()
    # print('nums = [4,5,6,7,0,1,2], target = 0:', s.search(nums = [4,5,6,7,0,1,2], target = 0))
    # print('nums = [4,5,6,7,0,1,2], target = 3:', s.search(nums = [4,5,6,7,0,1,2], target = 3))
    # print('nums = [1], target = 0:', s.search(nums = [1], target = 0))
    # print('nums = [1], target = 1:', s.search(nums = [1], target = 1))
    # print('nums = [1,3,5], target = 3:', s.search(nums = [1,3,5], target = 3))
    print('nums = [1,2,3,4,5,6], target = 4:', s.search(nums = [1,2,3,4,5,6], target = 4))
    print('nums = [8,1,2,3,4,5,6,7], target = 6:', s.search(nums = [8,1,2,3,4,5,6,7], target = 6))

if __name__ == '__main__':
    main()