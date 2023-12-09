from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        start with l = 0, r = 0
        increase r untill we get substring with every char; save 
        then increase l until there is every char
        when there is not every char, increase r again
        '''

        def is_counts_equal(t_char_counts, substr_char_counts):
            for key in t_char_counts.keys():
                if t_char_counts.get(key, 0) > substr_char_counts.get(key, 0):
                    return False
            return True
        
        l = 0
        r = 0 
        min_substr = ""

        t_char_counts = {}
        substr_char_counts = {}

        for char in t:
            t_char_counts[char] = t_char_counts.get(char, 0) + 1

        substr_char_counts[s[r]] = 1 + substr_char_counts.get(s[r], 0)
        
        while l < len(s) and r < len(s):

            if is_counts_equal(t_char_counts, substr_char_counts):
                if len(min_substr) > r - l + 1 or len(min_substr) == 0:
                    min_substr = s[l:r+1]
                substr_char_counts[s[l]] = substr_char_counts.get(s[l], 0) - 1
                l += 1
                continue
            elif l == len(s) - 1 and r == len(s) - 1:
                l += 1                
            if l < r and r == len(s) - 1:
                substr_char_counts[s[l]] = min(substr_char_counts.get(s[l], 0) - 1, 0)
                l += 1                
            elif r < len(s) - 1:
                r += 1
                substr_char_counts[s[r]] = 1 + substr_char_counts.get(s[r], 0)

        return min_substr
        
def main():
    s = Solution()
    print('s = "ADOBECODEBANC", t = "ABC":', s.minWindow(s = "ADOBECODEBANC", t = "ABC"))
    print('s = "a", t = "a":', s.minWindow(s = "a", t = "a"))
    print('s = "a", t = "aa":', s.minWindow(s = "a", t = "aa"))
    print('s = "ab", t = "b":', s.minWindow(s = "ab", t = "b"))
    print('s = "aa", t = "aa":', s.minWindow(s = "aa", t = "aa"))
    print('s = "abc", t = "b":', s.minWindow(s = "abc", t = "b"))

if __name__ == '__main__':
    main()