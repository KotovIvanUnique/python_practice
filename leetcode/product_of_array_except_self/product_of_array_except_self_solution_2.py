from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        product = 1
        for n in nums:
            result.append(product)
            product *= n

        product = 1
        for i in reversed(range(len(nums))):
            result[i] *= product
            product *= nums[i]
            
        return result

def main():
    s = Solution()
    print('nums = [-1,1,0,-3,3]:', s.productExceptSelf(nums = [1,2,3,4]))
    print('nums = [-1,1,0,-3,3]:', s.productExceptSelf(nums = [-1,1,0,-3,3]))

if __name__ == '__main__':
    main()