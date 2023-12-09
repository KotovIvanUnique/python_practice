from typing import List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        r = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
        
def main():
    s = Solution()
    print('s = "ABAB", k = 2:', s.characterReplacement(s = "ABAB", k = 2))
    print('s = "AABABBA", k = 1:', s.characterReplacement(s = "AABABBA", k = 1))

if __name__ == '__main__':
    main()