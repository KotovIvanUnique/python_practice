from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        prev = None
        
        for curr in nums:
            if prev == curr:
                return True
            else:
                prev = curr
        return False

def main():
    s = Solution()
    print(':', s.containsDuplicate([2,7,11,15]))
    print(':', s.containsDuplicate([2,7,11,15, 2]))

if __name__ == '__main__':
    main()