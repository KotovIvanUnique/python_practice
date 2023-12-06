from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_no_zeroes = 1
        count_zeroes = 0
        only_zeroes = True
        
        for el in nums:
            if el != 0:
                only_zeroes = False
            else:
                count_zeroes += 1
            product *= el
            product_no_zeroes = product_no_zeroes * el if el != 0 else product_no_zeroes
            
        if count_zeroes == 1:
            return [0 if el != 0 else product_no_zeroes for el in nums]
        elif only_zeroes or count_zeroes > 1:
            return [0 for el in nums]
        else:
            return [int(product/el) if el != 0 else product_no_zeroes for el in nums]

def main():
    s = Solution()
    print('nums = [-1,1,0,-3,3]:', s.productExceptSelf(nums = [1,2,3,4]))
    print('nums = [-1,1,0,-3,3]:', s.productExceptSelf(nums = [-1,1,0,-3,3]))

if __name__ == '__main__':
    main()