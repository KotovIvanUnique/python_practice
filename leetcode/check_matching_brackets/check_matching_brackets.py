class Solution:
    def __reverse(self, s: str) -> str:
        if s == '(':
            return ')'
        elif s == '[':
            return ']'
        elif s == '{':
            return '}'

    def is_valid(self, s: str) -> bool:
        if len(s)%2 == 0:
            string_dict = dict([(i, False) for i in range(len(s))])
            for i in range(len(s)):
                reverse_symbol = self.__reverse(s[i])
                for j in range(i+1,len(s),2):
                    if reverse_symbol == s[j] and string_dict[j] == False:
                        string_dict[i], string_dict[j] = True, True
                        break
            if False in string_dict.values():
                return False
            else:
                return True
        else:
            return False

def main():
    s = Solution()
    print('s="[]":', s.is_valid('[]'))
    print('s="(}){":', s.is_valid('(}){'))
    print('s="[(({}()){})]":', s.is_valid('[(({}()){})]'))

if __name__ == '__main__':
    main()