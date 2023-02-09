from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))
        
def main():
    s = Solution()
    print('[[9,9,4],[6,6,8],[2,1,1]]', s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
    print('[[3,4,5],[3,2,6],[2,2,1]]', s.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
    print('[[1]]', s.longestIncreasingPath([[1]]))

if __name__ == '__main__':
    main()