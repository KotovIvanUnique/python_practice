class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx_start = 0
        idx_end = 1
        len_s = len(s)

        if not s or len_s == 1 or len(s.strip()) == 0:
            return s
        elif len(set(s)) == 1:
            return s
        else:
            for i in range(len_s):
                if not idx_end - idx_start > len_s - i:
                    for j in range(i+1, len_s+1):
                        tmp = s[i:j]
                        if tmp == tmp[::-1]:
                            if j - i > idx_end - idx_start:
                                idx_start, idx_end = i, j
            return s[idx_start:idx_end]

def main():
    s = Solution()

    print('s = "babad"', s.longestPalindrome("babad"))
    print('s = "cbbd"', s.longestPalindrome("cbbd"))

if __name__ == '__main__':
    main()