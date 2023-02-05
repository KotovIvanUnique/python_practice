from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i, j in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, len(nums)-1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                
                elif s < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res
        
def main():
    s = Solution()
    print('[-1,0,1,2,-1,-4]:', s.threeSum([-1,0,1,2,-1,-4]))
    print('[0,1,1]:', s.threeSum([0,1,1]))
    print('[0,0,0]:', s.threeSum([0,0,0]))

if __name__ == '__main__':
    main()