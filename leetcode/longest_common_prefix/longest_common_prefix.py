from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        search_str = strs[0]
        max_prefix_length = 0

        if len(strs) == 1:
            return strs[0]
        else:
            for i in range(1, len(search_str)+1):
                prefix_length = 0
                for j in range(1, len(strs)):
                    if search_str[:i] == strs[j][:i] and len(search_str[:i]) == len(strs[j][:i]):
                        prefix_length = i
                    else:
                        prefix_length = 0
                        break
                max_prefix_length = max(prefix_length, max_prefix_length)
                if max_prefix_length == 0:
                    return ''
        return search_str[:max_prefix_length]

def main():
    s = Solution()
    print('strs = ["flower","flow","flight"]', s.longestCommonPrefix(["flower","flow","flight"]))
    print('strs = ["dog","racecar","car"]', s.longestCommonPrefix(["dog","racecar","car"]))

if __name__ == '__main__':
    main()