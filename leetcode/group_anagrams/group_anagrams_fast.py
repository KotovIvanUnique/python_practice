from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for e in strs:
            key = ''.join(sorted(e))
            groups[key] = groups.get(key, []) + [e]
            
        
        return list(groups.values())

def main():
    s = Solution()
    print(':', s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(':', s.groupAnagrams([""]))
    print(':', s.groupAnagrams(["a"]))
    print(':', s.groupAnagrams(["tea", "tea"]))
    print(':', s.groupAnagrams(["dis","sid","sid"]))

if __name__ == '__main__':
    main()