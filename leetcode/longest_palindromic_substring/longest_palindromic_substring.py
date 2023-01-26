# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         idx_start = 0
#         idx_end = 1
#
#         if len(set(s)) != 1:
#             for i in range(len(s)):
#                 for j in range(i+1, len(s)+1):
#                     tmp = s[i:j]
#                     if tmp == tmp[::-1]:
#                         if j - i > idx_end - idx_start:
#                             idx_start, idx_end = i, j
#             return s[idx_start:idx_end]
#         else:
#             return s

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         idx_start = 0
#         idx_end = 1
#         s_reversed = s[::-1]
#         len_s = len(s)
#
#         if len(set(s)) != 1:
#             for i in range(len_s):
#                 for j in range(len_s+1):
#                     if s[i:j] == s_reversed[len_s-j:len_s-i]:
#                         if j - i > idx_end - idx_start:
#                             idx_start, idx_end = i, j
#             return s[idx_start:idx_end]
#         else:
#             return s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        idx_start = 0
        idx_end = 1
        len_s = len(s)

        if len(set(s)) != 1:
            for i in range(0, len_s-1):
                window = 1
                if s[i] == s[i+1] and idx_end - idx_start < 2:
                    idx_start, idx_end = i, i + 2
                else:
                    while i-window >= 0 and i+window < len_s:
                        print('i:',s[i],'start:',s[i-window],'end:',s[i+window])
                        if s[i-window] == s[i+window]:
                            print('true')
                            window += 1
                        else:
                            print('false')
                            window -= 1
                            break
                    print('window:', window)
                    if idx_end - idx_start < (2 * window) + 1:
                        idx_start, idx_end = i-window, i+window+1
                        print('res:',s[idx_start:idx_end])
            return s[idx_start:idx_end]
        else:
            return s

def main():
    s = Solution()
    print('s = "babad"', s.longestPalindrome("babad"))
    # print('s = "cbbd"', s.longestPalindrome("cbbd"))
    # print('s = "c"', s.longestPalindrome("c"))
    # print('s = "aacabdkacaa"', s.longestPalindrome("aacabdkacaa"))

if __name__ == '__main__':
    main()