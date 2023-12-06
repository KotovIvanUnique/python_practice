from typing import List

class Solution:
    def get_counts(self, anagram: str) -> dict:
        counts = dict()

        for i in anagram:
            counts[i] = counts.get(i, 0) + 1

        return counts

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        group_number = 0
        matched = set()

        for i in range(len(strs)):
            curr_i = strs[i]
            if i in matched:
                continue
            else:
                group_number += 1
                matched.add(i)
                anagrams = [curr_i]
                counts_i = self.get_counts(curr_i)

                for j in range(i + 1, len(strs)):
                    curr_j = strs[j]

                    if j in matched:
                        continue
                    else:
                        if len(curr_i) == len(curr_j):
                            counts_j = self.get_counts(curr_j)

                            if counts_i == counts_j:
                                matched.add(j)
                                anagrams.append(curr_j)
                
                groups[group_number] = anagrams
        
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