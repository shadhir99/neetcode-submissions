class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''


        # stack = []

        # for char in s:
        #     if char in '({[':
        #         stack.append(char)
        #     elif char == '}':
        #         if not stack and stack[-1] != '{':
        #             return False
        #         stack.pop()
        #     elif char == ')':
        #         if not stack and stack[-1] != '(':
        #             return False
        #         stack.pop()
        #     elif char == ']':
        #         if not stack and stack[-1] != '[':
        #             return False
        #         stack.pop()
            
        # return stack == []


        stack = []
        hashmap = {'}':'{', ']':'[', ')':'('}

        for char in s:
            # Closing Character Condition
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
                
            


