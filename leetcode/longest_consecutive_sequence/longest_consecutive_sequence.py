from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums_len = len(nums)
        length = 1
        longest_length = 1

        if nums_len == 0:
            return 0
        else:
            for i in range(nums_len-1):
                if nums[i+1] - 1 == nums[i]:
                    length += 1
                elif nums[i+1] == nums[i]:
                    continue
                else:
                    longest_length = length if longest_length < length else longest_length
                    length = 1

            longest_length = length if longest_length < length else longest_length

            return longest_length

def main():
    s = Solution()
    print('nums = [100,4,200,1,3,2]', s.longestConsecutive(nums = [100,4,200,1,3,2]))
    print('nums = [0,3,7,2,5,8,4,6,0,1]', s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
    print('nums = [0,3,7,2,5,8,4,6,0,1]', s.longestConsecutive(nums = []))

if __name__ == '__main__':
    main()