from typing import List

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: List[str]) -> str:
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    """z
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            i = j + 1
            j = i + length
            res.append(str[i:j])
            i = j
            
        return res
        
def main():
    s = Solution()
    encoded = s.encode(['strr', 'st', 'strrrr'])
    print("['strr', 'st', 'strrrr']:", encoded)
    decoded = s.decode(encoded)
    print(encoded + ':', s.decode(encoded))

if __name__ == '__main__':
    main()