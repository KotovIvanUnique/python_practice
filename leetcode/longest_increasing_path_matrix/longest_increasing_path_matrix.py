from typing import List
from itertools import product

class Solution:
    def invalid(self, i, j, n, m):
            return i < 0 or j < 0 or i == n or j == m

    def make_move(self, matrix: List[List[int]], n: int, m: int, i: int, j: int, current_path: int, paths: List, dirs: List):        
        # print('i', i, 'j', j, 'current', matrix[i][j], 'current_path', current_path)
        for dx, dy in dirs:
            r, c = i + dx, j + dy
            if not self.invalid(r, c, n, m) and matrix[r][c] > matrix[i][j]:
                self.make_move(matrix, n, m, r, c, current_path + 1, paths, dirs)
            else:
                paths.append(current_path + 1)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longest_path = 1
        n, m = len(matrix), len(matrix[0])
        for i, j in list(product(range(n), range(m))):
            paths = []
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            self.make_move(matrix, n, m, i, j, 0, paths, dirs)
            longest_path = max(longest_path, max(paths))
        return longest_path

def main():
    s = Solution()
    print('[[9,9,4],[6,6,8],[2,1,1]]', s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
    print('[[3,4,5],[3,2,6],[2,2,1]]', s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
    print('[[1]]', s.longestIncreasingPath([[1]]))

if __name__ == '__main__':
    main()