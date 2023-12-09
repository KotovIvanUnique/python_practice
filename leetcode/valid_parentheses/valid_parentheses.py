from typing import List

class Solution:
    def isValid(self, s: str) -> bool:            
        mapping = {")": "(", "]": "[", "}": "{"}

        opening = []
        for l in s:
            if l in mapping:
                if not opening or opening[-1] != mapping[l]:
                    return False
                else:
                    opening.pop()
            else:
                opening.append(l)
        return not opening
        
def main():
    s = Solution()    
    print('s = "():"', s.isValid(s = "()"))
    print('s = "()[]{}":', s.isValid(s = "()[]{}"))
    print('s = "(]":', s.isValid(s = "(]"))
    print('s = "((({}[()])))":', s.isValid(s = "((({}[()])))"))
    print('s = "((({{{]]])))}}}":', s.isValid(s = "((({{{]]])))}}}"))
    print('s = "((":', s.isValid(s = "(("))

if __name__ == '__main__':
    main()