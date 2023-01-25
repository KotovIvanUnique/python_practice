class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_char = 1
        len_s = len(s)
        if len_s == 0:
            return 0
        else:
            for i in range(len_s):
                cnt_char = 1
                characters = [s[i]]
                for j in range(i+1, len_s):
                    if s[j] not in characters:
                        cnt_char += 1
                    else:
                        break
                    characters.append(s[j])
                max_char = max(cnt_char, max_char)
            return max_char

def main():
    s = Solution()
    print('s = "abcabcbb":', s.lengthOfLongestSubstring('abcabcbb'))
    print('s = "bbbbb":', s.lengthOfLongestSubstring('bbbbb'))
    print('s = "pwwkew":', s.lengthOfLongestSubstring('pwwkew'))

if __name__ == '__main__':
    main()