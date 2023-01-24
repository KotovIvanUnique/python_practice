from typing import List

class Solution:
    def __get_strength_dict(self, mat: List[List[int]]) -> dict:
        strength = {}
        for i in range(len(mat)):
            strength[i] = sum(mat[i])
        return strength

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = self.__get_strength_dict(mat)
        result = [x for x in range(len(mat))]

        for i in range(len(result)):
            for j in range(len(result)):
                tmp_i = result[i]
                tmp_j = result[j]

                if strength.get(tmp_i) < strength.get(tmp_j):
                    result[i] = tmp_j
                    result[j] = tmp_i
                elif strength.get(result[i]) == strength.get(result[j]) and result[i] < result[j]:
                    result[i] = tmp_j
                    result[j] = tmp_i

        return result[:k]

def main():
    s = Solution()
    print("""
    [[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,1]]""",
    s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))
    print("""
    [[1,0,0,0],
     [1,1,1,1],
     [1,0,0,0],
     [1,0,0,0]]""",
    s.kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2))

if __name__ == '__main__':
    main()