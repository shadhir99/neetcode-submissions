class Solution:
    def isValid(self, s: str) -> bool:
        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # return s == ''


        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif char == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            
        return not stack

