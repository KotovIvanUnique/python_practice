from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
def main():
    s = Solution()
    print(':', s.containsDuplicate([2,7,11,15]))
    print(':', s.containsDuplicate([2,7,11,15, 2]))

if __name__ == '__main__':
    main()