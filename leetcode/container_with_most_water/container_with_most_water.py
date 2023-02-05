from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        ordered_by_height = sorted([(i, height[i]) for i in range(len(height))], key=lambda x: x[1], reverse=True)
        left = ordered_by_height[0][0]
        right = ordered_by_height[0][0]

        for i in ordered_by_height:
            left = min(i[0], left)
            right = max(i[0], right)        
            max_area = max(max_area, i[1] * max(i[0] - left, right - i[0]))
            if max_area > len(height) * height[i[0]]:
                return max_area
        return max_area  

def main():
    s = Solution()
    print('[1,8,6,2,5,4,8,3,7]:', s.maxArea([1,8,6,2,5,4,8,3,7]))
    print('[1,1]:', s.maxArea([1,1]))

if __name__ == '__main__':
    main()